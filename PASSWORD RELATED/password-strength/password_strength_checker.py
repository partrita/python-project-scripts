import re



def evaluate_strength(input_text):
    """
        Checks the strength of a password and returns a tuple containing the strength score
        and improvement messages.
    """
    # Minimum password length
    min_length = 8

    # Regular expressions to check for different character types
    has_lowercase = re.compile(r'[a-z]')
    has_uppercase = re.compile(r'[A-Z]')
    has_digit = re.compile(r'\d')
    has_special = re.compile(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?/\\|]')

    score = 0
    feedback_msgs = []

    if len(input_text) >= min_length:
        score += 1
    else:
        feedback_msgs.append("Password should have at least {} characters.".format(min_length))

    if has_lowercase.search(input_text):
        score += 1
    else:
        feedback_msgs.append("Password should have at least one lowercase letter.")

    if has_uppercase.search(input_text):
        score += 1
    else:
        feedback_msgs.append("Password should have at least one uppercase letter.")

    if has_digit.search(input_text):
        score += 1
    else:
        feedback_msgs.append("Password should have at least one digit.")

    if has_special.search(input_text):
        score += 1
    else:
        feedback_msgs.append("Password should have at least one special character.")

    return score, feedback_msgs


if __name__ == "__main__":
    pwd_input = input("Enter your password: ")
    score_val, feedback = evaluate_strength(pwd_input)

    print("\nPassword Strength: {}".format(score_val))
    if score_val == 5:
        print("Password is very strong!")
    else:
        print("Password needs improvement:")
        for rule in feedback:
            print("- {}".format(rule))
