"""
Filename:         player.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page handles the users move in the Tic-tac-toe game.
"""

import board as b

def player_move():
        """Get and validate player's move (1-9). Updates board with 'X'."""
        
        print('\nMove')
        invalid = True
        
        while invalid == True:
            move = int(input('Enter a move between 1 - 9: '))
            if 1 <= move <= 9 and b.game[move-1] == '*':
                b.game[move-1] = 'X'
                invalid = False
            
            