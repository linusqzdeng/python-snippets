x = int(input('Please enter an integer'))
if x < 0:
    x = 0
    print('Please change it to positive')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
