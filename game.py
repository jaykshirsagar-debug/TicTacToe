from bot import bot_move
import board as b
from player import player_move

game_over = False
num_moves = 0

def check_game_over():
    """Checks if game is over by win condition or draw.
    Returns:
        bool: True if game is over, False if game continues
    """
    global game_over
    global num_moves
    #The game requires a minimum of 5 moves to be over
    #Only starts to check win after 5 or more moves
    if num_moves >= 5:

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
    else:
        num_moves += 1
    
    return game_over
    
b.show_board()

while game_over == False:
    """
    Game loop until either Player or Bot wins.
    if the game is over, while loop will be exited.
    """

    if check_game_over() == False:
        player_move()
        
    if check_game_over() == False:
        bot_move()
        

b.show_board()
