'''
    if_else practice: account_password
'''

ACCOUNT = 'linus00012'
PASSWORD = '12123355'

print('Please input your username and password')
user_account = input('username: ')
user_password = input('password: ')

if user_account == ACCOUNT and user_password == PASSWORD:
    print('Successfully access to your account')
else:
    print('Either username or password is wrong')