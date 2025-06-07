"""
Filename:         board.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page displays the state of board after either the player or bot moves, and after the game ends.
"""

game = ['*','*','*',
        '*','*','*',
        '*','*','*',]

def show_board():
    """Displays the current state of the Tic-Tac-Toe board in a grid format."""
    print(f'{game[0]}  {game[1]}  {game[2]}')
    print(f'{game[3]}  {game[4]}  {game[5]}')
    print(f'{game[6]}  {game[7]}  {game[8]}')