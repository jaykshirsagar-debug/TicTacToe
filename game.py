from comp_move import bot_move
import board as b
from player import player_move

game_over = False

def check_game_over():
    global game_over
    if (b.game[0] == b.game[1] == b.game[2] == 'X') or (b.game[0] == b.game[1] == b.game[2] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[2] == b.game[5] == b.game[8] == 'X') or (b.game[2] == b.game[5] == b.game[8] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[6] == b.game[7] == b.game[8] == 'X') or (b.game[6] == b.game[7] == b.game[8] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[0] == b.game[3] == b.game[6] == 'X') or (b.game[0] == b.game[3] == b.game[6] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[0] == b.game[4] == b.game[8] == 'X') or (b.game[0] == b.game[4] == b.game[8] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[2] == b.game[4] == b.game[6] == 'X') or (b.game[2] == b.game[4] == b.game[6] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[3] == b.game[4] == b.game[5] == 'X') or (b.game[3] == b.game[4] == b.game[5] == 'O'):
        print('---- Game Over ----')
        game_over = True
    elif (b.game[1] == b.game[4] == b.game[7] == 'X') or (b.game[1] == b.game[4] == b.game[7] == 'O'):
        print('---- Game Over ----')
        game_over = True

    if '*' not in b.game and game_over == False:
        print('---- Game Over - Draw ----')
        game_over = True
    


    
b.show_board()

while game_over == False:
    player_move()
    check_game_over()
    bot_move()
    check_game_over()

b.show_board()