import board as b
import random as rd

def bot_move():
    """
    Make bot move by randomly selecting empty spot on board.
    """
    valid_move = False
    while valid_move == False:
        random_move = rd.randint(1,9)
        if b.game[random_move - 1] == '*':
            b.game[random_move - 1] = 'O'
            b.show_board()
            valid_move = True