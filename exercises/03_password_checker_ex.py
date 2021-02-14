# Create a password length checker

username = input('Enter a username: ')
password = input('Enter a password: ')

password_length = len(password)
masked_password = 'x' * len(password)

print(f'Hi {username}! your password {masked_password} is {password_length} characters long.')