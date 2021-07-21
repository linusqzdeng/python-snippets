my_list = list(range(0,101))
num = int(input('Please give a number: '))
guess = 50
attempt = 0

print('''Let me guesse what integer you\'ve got from 1 to 100.
    My first guess is 50.''')

while guess in my_list:
    centre_len = int(len(my_list)/2)
    guess = my_list[centre_len-1]
    answer = input('Is it too high, too small or bingo: ')
    if answer == 'too high':
        my_list = my_list[:centre_len]
        print('My guess is now: ', guess)
    elif answer == 'too small':
        my_list = my_list[centre_len:]
        print('My guess is now: ', guess)
    attempt += 1

if guess == num:
    print('The number you got is: ', guess)
else:
    print('Failed to find the number.')
print('I have try ' + str(attempt) + ' times to make it!')