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
    "OTHERS", "gemini chatbot", "generate_book.py", "LICENSE", "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "pixi.lock", "pixi.toml", "file.txt"
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

def get_projects(category_path):
    projects = []
    if not category_path.exists():
        return []

    for item in category_path.iterdir():
        if item.name.startswith("."):
            continue
        if item.is_dir():
            projects.append(item)
        elif item.suffix == ".py":
            projects.append(item)
    return sorted(projects, key=lambda x: x.name)

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

    files = list(project_path.glob("*.py"))
    if not files:
        return None
    
    # Try to find main.py or project_name.py
    for f in files:
        if f.name == "main.py":
            return f
    
    folder_name = project_path.name
    for f in files:
        if f.name == f"{folder_name}.py":
            return f
        
    return files[0]

def generate_qmd(category_path, project_path):
    readme_path = find_readme(project_path)
    script_path = find_main_script(project_path)
    
    # If project_path is a file, the project name is the filename without extension
    project_name = project_path.stem if project_path.is_file() else project_path.name
    
    content = []
    content.append(f"# {project_name}")
    content.append("")
    
    if readme_path:
        try:
            with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
                readme_content = f.read()
                
                # Sanitize to prevent YAML parsing errors
                readme_content = re.sub(r'^---$', '***', readme_content, flags=re.MULTILINE)
                
                # Fix relative image paths
                # Heuristic: Find <img src="path"> or ![alt](path)
                # and prefix path with the project's original location relative to mybook/projects/category/project.qmd
                # From mybook/projects/category/project.qmd, the root is ../../../
                # So the original project path is ../../../category/project_name/
                
                def fix_path(match):
                    prefix = match.group(1)
                    path = match.group(2)
                    suffix = match.group(3)
                    
                    if path.startswith(('http', '/', '#')):
                        return match.group(0)
                    
                    # Decode URL-encoded paths (e.g., %2F -> /)
                    import urllib.parse
                    decoded_path = urllib.parse.unquote(path)
                    
                    # New path relative to the .qmd file
                    new_path = f"../../../{category_path.name}/{project_path.name}/{decoded_path}"
                    return f"{prefix}{new_path}{suffix}"

                # Markdown images: ![alt](path)
                readme_content = re.sub(r'(!\[.*?\]\()(.*?)(\))', fix_path, readme_content)
                # HTML images: <img ... src="path" ... >
                readme_content = re.sub(r'(<img.*?src=["\'])(.*?)(["\'].*?>)', fix_path, readme_content)

                content.append(readme_content)
                content.append("")
        except Exception as e:
            print(f"Error reading README for {project_name}: {e}")

    if script_path:
        try:
            with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
                script_content = f.read()
                content.append(f"## Source Code: {script_path.name}")
                content.append("```python")
                content.append(script_content)
                content.append("```")
                content.append("")
        except Exception as e:
            print(f"Error reading script for {project_name}: {e}")
    
    # Output path
    output_dir = BOOK_DIR / "projects" / category_path.name
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{project_name}.qmd"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        
    return f"projects/{category_path.name}/{project_name}.qmd"

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

    # Generate _quarto.yml using yaml.dump
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
