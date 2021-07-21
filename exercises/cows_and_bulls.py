'''
    This program plays the 'cows and bulls' game. 
    How to play:
        1. Randomly generate a 4-digit number and ask the user to guess.
        2. For every digit that the user guessed correctly in the correct place:
            they have a cow
        3. For every digit that the user guessed correctly in the wrong place:
            they have a bull
        4. Every time the user makes a guess, Python will tell them how many 'cows'
        and 'bulls' they have.
'''

import random

num = str(random.randint(1000, 9999))
cows_num = 0
bulls_num = 0
gueesses = 1

def cowsNbulls(guess_number):
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if guess_number[i] == num[i]:
            cows += 1
        elif guess_number[i] in num:
            bulls += 1
    return cows, bulls

if __name__ == '__main__':
    while True:
        guess = input('Give me a 4 digit number:\n')
        cow, bull = cowsNbulls(guess)
        print(cow, 'cows,', bull, 'bulls')

        if cow == 4:
            print('Bingo! You\'ve got the correct number', num)
            print('You\'ve taken', gueesses, 'gueeses in total')
            break
        else:
            gueesses += 1
