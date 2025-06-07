"""
Filename:         bot.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page handles the bots move in the Tic-tac-toe game.
"""

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