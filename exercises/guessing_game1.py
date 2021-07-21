'''
This program generates a random number between 1 to 9 (including 1 and 9) and asks the user to
guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''

from random import randint

num = randint(1, 9)
attempt = 1

while True:
    guess = int(input('Guess what number I have got from 1 to 9?\n'))
    if guess not in list(range(1, 10)):
        print('Invalid input. You must select a number between 1 to 9.')
        attempt += 1
        continue
    if guess > num:
        print('Too high! Try again!')
        attempt += 1
        continue
    elif guess < num:
        print('Too low! Try again!')
        attempt += 1
        continue
    elif guess == num:
        print('Bingo!')
        if input('Do you want to start again? Type \'exit\' to quit\n') == 'exit':
            print('Game over! You have tried', attempt, 'times to win.')
            break
        else:
            attempt = 1
            continue
    else:
        print('Please choose a number between 1 to 9.')
        attempt += 1
        continue
