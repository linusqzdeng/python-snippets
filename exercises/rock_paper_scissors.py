'''
This program asks for players play rock paper scissors game. Compare them, print out 
a message of congratulations to the winnerm and ask if the players want to start a new game.
'''

def rps(player1, player2):
    if player1 == player2:
        return('Draw! Please start again!')
    elif player1 == 'rock':
        if player2 == 'scissors':
            return('Congrat! Player1 is the winner!')
        else:
            return('Congrat! Player2 is the winner!')
    elif player1 == 'scissors':
        if player2 == 'rock':
            return('Congrat! Player2 is the winner!')
        else:
            return('Congrat! Player1 is the winner!')
    elif player1 == 'paper':
        if player2 == 'rock':
            return('Congrat! Player1 is the winner!')
        else:
            return('Congrat! Player2 is the winner!')
    else:
        return('Invalid input. Please follow the instruction.')

user1 = input('Which one do you want to choose? Rock, scissors or paper? ')
user2 = input('Which one do you want to choose? Rock, scissors or paper? ')

print(rps(user1, user2))
