import os
import shutil
import yaml
import re
from pathlib import Path

# Configuration
REPO_ROOT = Path(".")
BOOK_DIR = Path("mybook")
EXCLUDE_DIRS = {
    ".git", ".github", ".pixi", "mybook", "__pycache__", ".ipynb_checkpoints", 
    ".vscode", ".idea", "venv", "env", "node_modules", "site-packages",
    "gemini chatbot", "generate_book.py", "LICENSE", "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "pixi.lock", "pixi.toml", "file.txt"
}

def get_categories():
    categories = []
    for item in REPO_ROOT.iterdir():
        if item.name in EXCLUDE_DIRS:
            continue
        if item.name.startswith("."):
            continue
        if item.is_dir():
            categories.append(item)
    return sorted(categories, key=lambda x: x.name)

def find_readme(project_path):
    if project_path.is_file():
        return None
    for file in project_path.iterdir():
        if file.name.lower().startswith("readme") and file.is_file():
            return file
    return None

def find_main_script(project_path):
    if project_path.is_file():
        return project_path

    # Support .py and .sip
    files = list(project_path.glob("*.py")) + list(project_path.glob("*.sip"))
    if not files:
        return None
    
    # Try to find main.py or project_name.py
    for f in files:
        if f.name in ["main.py", "index.py", f"{project_path.name}.py", f"{project_path.name}.sip"]:
            return f
    
    return files[0]

def get_projects(category_path):
    projects = []
    if not category_path.exists():
        return []

    # Recursively find projects if it's OTHERS or deep structure
    def find_projects_rec(path, depth=0):
        if depth > 10: return # Increased depth for deep SIP paths
        try:
            for item in path.iterdir():
                if item.name.startswith(".") or item.name in EXCLUDE_DIRS:
                    continue
                if item.is_dir():
                    # If it has a readme or a script, it's a project
                    if find_readme(item) or any(item.glob("*.py")) or any(item.glob("*.sip")):
                        projects.append(item)
                    # Even if it's a project, it might have subprojects (like OTHERS/Jarvis)
                    find_projects_rec(item, depth + 1)
                elif item.suffix in [".py", ".sip"]:
                    projects.append(item)
        except PermissionError:
            pass

    if category_path.name == "OTHERS":
        find_projects_rec(category_path)
    else:
        for item in category_path.iterdir():
            if item.name.startswith(".") or item.name in EXCLUDE_DIRS:
                continue
            if item.is_dir():
                projects.append(item)
            elif item.suffix in [".py", ".sip"]:
                projects.append(item)
    
    # Use set to avoid duplicates and return sorted list
    unique_projects = []
    seen = set()
    for p in projects:
        if p not in seen:
            unique_projects.append(p)
            seen.add(p)
    
    return sorted(unique_projects, key=lambda x: str(x))

def generate_qmd(category_path, project_path):
    # If project_path is a file, the project name is the filename without extension
    project_name = project_path.stem if project_path.is_file() else project_path.name
    
    # For projects deep in OTHERS, use a flattened name for the file
    try:
        rel_to_cat = project_path.relative_to(category_path)
        output_name = "_".join(rel_to_cat.parts).replace(".sip", "").replace(".py", "")
    except ValueError:
        output_name = project_name

    output_dir = BOOK_DIR / "projects" / category_path.name
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{output_name}.qmd"
    
    # Check if we should skip
    if output_file.exists():
        return f"projects/{category_path.name}/{output_name}.qmd"

    readme_path = find_readme(project_path)
    script_path = find_main_script(project_path)
    
    content = []
    readme_content = ""
    
    if readme_path:
        try:
            with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
                readme_content = f.read()
                readme_content = re.sub(r'^---$', '***', readme_content, flags=re.MULTILINE)
                
                def fix_path(match):
                    prefix, path, suffix = match.groups()
                    if path.startswith(('http', '/', '#', 'mailto:')): return match.group(0)
                    import urllib.parse
                    decoded_path = urllib.parse.unquote(path)
                    new_path = f"../../../{project_path.relative_to(REPO_ROOT)}/{decoded_path}"
                    return f"{prefix}{new_path}{suffix}"

                readme_content = re.sub(r'(\!??\[.*?\]\()(.*?)(\))', fix_path, readme_content)
                readme_content = re.sub(r'(<img.*?src=["\'])(.*?)(["\'].*?>)', fix_path, readme_content)
                readme_content = re.sub(r'(?<!\\)@', r'&#64;', readme_content)
        except Exception as e:
            print(f"Error reading README for {project_name}: {e}")

    # More robust check for repeated title
    has_title_in_readme = False
    if readme_content:
        norm_content = readme_content.replace('\\n', '\n')
        lines = norm_content.splitlines()
        # Check first 5 non-empty lines for a title
        count = 0
        for line in lines:
            stripped = line.strip()
            if not stripped: continue
            if stripped.startswith("#"):
                header_text = stripped.lstrip('#').strip()
                header_text = re.sub(r'^(Title|Project|Name):\s*', '', header_text, flags=re.IGNORECASE).strip(' "\'*')
                clean_header = re.sub(r'[^\w\s]', '', header_text).lower()
                clean_project = re.sub(r'[^\w\s]', '', project_name).lower()
                if clean_header == clean_project or clean_header == clean_project.replace(' ', '') or clean_project in clean_header:
                    has_title_in_readme = True
                    break
            count += 1
            if count > 5: break

    if readme_content:
        if has_title_in_readme:
            # Find the first H1 and keep it, lower others
            lines = readme_content.splitlines()
            new_lines = []
            found_first = False
            for line in lines:
                if line.startswith("# ") and not found_first:
                    new_lines.append(line)
                    found_first = True
                elif line.startswith("#"):
                    new_lines.append("#" + line)
                else:
                    new_lines.append(line)
            readme_content = "\n".join(new_lines)
        else:
            # Lower all headers
            readme_content = re.sub(r'^#', '##', readme_content, flags=re.MULTILINE)

    if not has_title_in_readme:
        content.append(f"# {project_name}")
        content.append("")
    
    if readme_content:
        content.append(readme_content)
        content.append("")
    else:
        # Add a default description if README is missing
        content.append(f"This project contains scripts related to **{project_name}**.")
        content.append("")

    if script_path:
        try:
            with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
                script_content = f.read()
                content.append(f"## Source Code: {script_path.name}")
                lang = "python" if script_path.suffix == ".py" else "cpp"
                content.append(f"```{lang}")
                content.append(script_content)
                content.append("```")
                content.append("")
        except Exception as e:
            print(f"Error reading script for {project_name}: {e}")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        
    return f"projects/{category_path.name}/{output_name}.qmd"

def main():
    if not BOOK_DIR.exists():
        BOOK_DIR.mkdir()

    categories = get_categories()
    chapters_config = ["index.qmd"]
    
    print(f"Found {len(categories)} categories.")

    for category_path in categories:
        projects = get_projects(category_path)
        if not projects:
            continue
            
        category_chapter = {
            "part": category_path.name,
            "chapters": []
        }
        
        for project_path in projects:
            qmd_rel_path = generate_qmd(category_path, project_path)
            category_chapter["chapters"].append(qmd_rel_path)
            
        if category_chapter["chapters"]:
            chapters_config.append(category_chapter)

    chapters_config.append("references.qmd")

    # Generate _quarto.yml
    quarto_config = {
        "project": {
            "type": "book",
            "output-dir": "_book"
        },
        "execute": {
            "enabled": False
        },
        "book": {
            "title": "Python Project Scripts",
            "author": "Repo Contributors",
            "date": "today",
            "chapters": chapters_config
        },
        "bibliography": "references.bib",
        "format": {
            "html": {
                "theme": "cosmo",
                "toc": True,
                "number-sections": False
            }
        }
    }

    with open(BOOK_DIR / "_quarto.yml", "w", encoding="utf-8") as f:
        yaml.dump(quarto_config, f, sort_keys=False, allow_unicode=True)
        
    # Generate index.qmd
    index_path = BOOK_DIR / "index.qmd"
    if not index_path.exists():
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("# Introduction\n\nThis book is a compilation of Python projects from the repository.\n")

    print("Quarto book generated successfully.")

if __name__ == "__main__":
    main()
