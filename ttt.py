import random as rd

game = ['*','*','*',
        '*','*','*',
        '*','*','*',]

def show_board():
    print(f'{game[0]} | {game[1]} | {game[2]}')
    print('----------')
    print(f'{game[3]} | {game[4]} | {game[5]}')
    print('----------')
    print(f'{game[6]} | {game[7]} | {game[8]}')

show_board()

invalid = True

while invalid == True:
    first = input('\nDo you want to go first (y/n)?:')
    if first == 'y':
        print('You are going first')
        invalid = False
    elif first == 'n':
        print('You are going second')
        invalid = False

print('\nMove')
move = int(input('Enter a move between 1 - 9: '))

if 1 <= move <= 9 and game[move-1] == '*':
    game[move-1] = 'X'
    show_board()
else:
    print('Invalid move!')