import string
import secrets
import hashlib

# Define the set of characters to be used in the password
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Generate a random password of the specified length and its PBKDF2-HMAC-SHA256 hash."""
    password = ''.join(secrets.choice(CHARACTER_SET) for i in range(length))
    # Hash password with PBKDF2-HMAC-SHA256 to avoid weak hashing issues
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ).hex()
    return password, password_hash

def main():
    # Prompt the user for the number of items to generate and their length
    while True:
        try:
            count = int(input("How many passwords do you want to generate? "))
            length = int(input("Enter the length of the password(s): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue 
    # Generate the specified number of passwords without logging clear-text passwords
    print("Generated passwords:")
    for i in range(count):
        generate_password(length)
        print(f"{i+1}. Password generated successfully (length: {length}).")

if __name__ == "__main__":
    main()
