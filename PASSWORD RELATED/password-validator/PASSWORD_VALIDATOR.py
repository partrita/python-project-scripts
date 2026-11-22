import string


def passwordValidator():
    """
    Validates passwords to match specific rules
    : return: str
    """
    # display rules that a password must conform to
    print('\nYour password should: ')
    print('\t- Have a minimum length of 6;')
    print('\t- Have a maximum length of 12;')
    print('\t- Contain at least an uppercase letter or a lowercase letter')
    print('\t- Contain at least a number;')
    print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
    print('\t- Not contain space(s).')
    # get user's password (never log or display the raw password)
    userPassword = input('\nEnter a valid password: ').strip()
    # check if user's password conforms 
    # to the rules above
    if not(6 <= len(userPassword) <= 12):
        print('Invalid Password..your password should have a minimum length of 6 and a maximum length of 12')
        return False
    if ' ' in userPassword:
        print("Invalid Password..your password shouldn't contain space(s)")
        return False
    if not any(i in string.ascii_letters for i in userPassword):
        print('Invalid Password..your password should contain at least an uppercase letter and a lowercase letter')
        return False
    if not any(i in string.digits for i in userPassword):
        print('Invalid Password..your password should contain at least a number')
        return False
    if not any(i in string.punctuation for i in userPassword): 
        print('Invalid Password..your password should contain at least a special character')
        return False
    else:
        print('Valid Password!')
        return True

# Securely validate without exposing password in logs
passwordValidator()