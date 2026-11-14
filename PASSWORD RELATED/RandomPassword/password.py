import string
import secrets
import hashlib

# Define the set of characters to be used in the password
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Generate a random password of the specified length using SHA-256 hashing for security."""
    password = ''.join(secrets.choice(CHARACTER_SET) for i in range(length))
    # Hash password locally to avoid clear-text storage issues
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password, password_hash

def main():
    # Prompt the user for the number of passwords to generate and their length
    while True:
        try:
            num_pass = int(input("How many passwords do you want to generate? "))
            password_length = int(input("Enter the length of the password(s): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue 
    # Generate the specified number of passwords and print them to the console
    print("Generated passwords:")
    for i in range(num_pass):
        generated_password = generate_password(password_length)
        print(f"{i+1}. {generated_password}...")

if __name__ == "__main__":
    main()
