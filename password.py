def check_password(password):
    # finds how many numbers are in the password
    numbers = sum(c.isdigit() for c in password)
    if (numbers == 0) and (len(password) <= 6):
        return 'Weak Password add at least 7 letters and a number'
    elif (numbers == 0) and (len(password) >= 7):
        return 'Medium Password Try to add 1 number or more'
    elif (numbers > 0) and (len(password) >= 7):
        return 'Strong Password'
    else: 'What kind of password is this'

while True:
    # gets password from user
    password1 = input('Type your password here: ')
    # checks if the user has a strong password
    if check_password(password1) == 'Strong Password':
        print('Strong Password')
        # asks if they want to try another
        new_password = input('Want to Try another Password? (Y/N) ')
        # checks if they answer no and breaks the while loop
        if (new_password == 'N') or (new_password == 'n'):
            print('Goodbye!')
            break
        else: continue
    # Prints the result
    print(check_password(password1))
