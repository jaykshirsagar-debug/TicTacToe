import board as b

def player_move():
        print('\nMove')

        invalid = True
        
        while invalid == True:
            move = int(input('Enter a move between 1 - 9: '))
            if 1 <= move <= 9 and b.game[move-1] == '*':
                b.game[move-1] = 'X'
                invalid = False
            
            