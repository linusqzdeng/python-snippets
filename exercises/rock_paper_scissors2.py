print('''Please selct one of the followings:
        rock
        scissors
        paper''')

while True:
    dict_rps = {'rock': 1, 'paper': 2, 'scissors': 3}

    player1 = input('Player1: ')
    player2 = input('Player2: ')
    
    a = dict_rps.get(player1)
    b = dict_rps.get(player2)
    diff = a - b

    if diff in [-2, 1]:
        print('Player1 win this game!')
        if input('Do you want to play again? ') == 'yes':
            continue
        else:
            print('Game over')
            break
    elif diff in [2, -1]:
        print('Player2 win this game!')
        if input('Do you want to play again? ') == 'yes':
            continue
        else:
            print('Game over')
            break
    else:
        print('Draw! Please start again!')
        continue
