import hashlib

# Algorithms considered insecure for password hashing
WEAK_ALGORITHMS = {'md5', 'md4', 'sha1', 'sha'}

def get_hashed_password(password, algorithm='sha256', salt=None):
    """
    Hashes the input password using a secure key derivation function (PBKDF2)
    or specified secure hashing algorithm.

    Args:
        password (str): The input password to be hashed.
        algorithm (str): The hashing algorithm to use (default is SHA-256).
        salt (bytes, optional): Salt for hashing. If None, a random salt is generated.

    Returns:
        str: The hashed password as a hexadecimal string.
    """
    algorithm_lower = algorithm.lower()
    if algorithm_lower in WEAK_ALGORITHMS:
        raise ValueError(f"Insecure hashing algorithm '{algorithm}' is not permitted for password hashing.")
    if algorithm_lower not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

    if salt is None:
        import os
        salt = os.urandom(16)
    # Using PBKDF2-HMAC with 100,000 iterations for secure password hashing
    derived = hashlib.pbkdf2_hmac(algorithm_lower, password.encode('utf-8'), salt, 100000)
    return salt.hex() + '$' + derived.hex()

if __name__ == "__main__":
    print("Password Hashing Utility")
    print("------------------------")

    password = input("Enter your password: ")

    try:
        algorithm = 'sha256'
        hashed_password = get_hashed_password(password, algorithm)
        print(f"Hashed password (using PBKDF2-{algorithm.upper()}): {hashed_password}")
    except ValueError as e:
        print(e)
