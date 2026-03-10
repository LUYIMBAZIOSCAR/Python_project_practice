print('--Password Checker --')

def check_password ():
    password=input('Please enter your password : ')

    # checking if it contains atleast eight characters 
    # We use the len() function 
    if len(password) < 8:
        print('Password must contain atleast 8 characters ')
    elif not any(char.isdigit() for char in password):
        print('Password must contain a number ')
    elif not any(char.isupper() for char in password):
        print('password must contain an uppercase letter ')
    else:
        print('Password is strong')
    


check_password()


