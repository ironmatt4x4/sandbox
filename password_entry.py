'''Mattt'''

MIN_LENGTH = 6
password = input('Enter a password with 6 or more characters')

password_length = len(password)
if password_length < MIN_LENGTH:
    print('Error: password too short')
else:
    for i in range(0, password_length, 1):
        print('*', end='')
