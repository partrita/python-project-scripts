import string

def mask_password(password):
    """Mask a password for safe display, showing only first 2 chars and masking the rest."""
    if len(password) <= 2:
        return '*' * len(password)
    return password[:2] + '*' * (len(password) - 2)

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
   # get user's password
    userPassword = input('\nEnter a valid password: ').strip()
   # check if user's password conforms 
   # to the rules above
    if not(6 <= len(userPassword) <= 12):
        message = 'Invalid Password..your password should have a minimum '
        message += 'length of 6 and a maximum length of 12'
        return message
    if ' ' in userPassword:
       message = 'Invalid Password..your password shouldn\'t contain space(s)'
       return message
    if not any(i in string.ascii_letters for i in userPassword):
       message = 'Invalid Password..your password should contain at least '
       message += 'an uppercase letter and a lowercase letter'
       return message
    if not any(i in string.digits for i in userPassword):
        message = 'Invalid Password..your password should contain at least a number'
        return message
    if not any(i in string.punctuation for i in userPassword): 
       message = 'Invalid Password..your password should contain at least a special character'
       return message
    else:
        masked = mask_password(userPassword)
        return f'Valid Password! (Displayed: {masked})'

my_validation_result = passwordValidator()
# Display validation result without exposing the actual password
print(my_validation_result)