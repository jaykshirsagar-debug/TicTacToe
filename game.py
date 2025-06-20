"""
Filename:         game.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This Python program implements a Tic-tac-toe game where a player competes against a bot of their choice.
                 The game tracks moves, validates win conditions, and handles game completion.
"""


from bot import Bots
import board as b
from player import player_move

bot = Bots()
choice = False
difficulty = 0

while choice == False:
    print('Difficulty:')
    print(' 1. Brain Dead')
    print(' 2. Noob')
    input = int(input())

    if input == 1:
        difficulty = 1
        print('Brain Dead difficulty selected')
        choice = True
    elif input == 2:
        difficulty = 2
        print('Noob difficulty selected')
        choice = True

b.show_board()

while b.game_over == False:
    """
    Game loop until either Player or Bot wins.
    if the game is over, while loop will be exited.
    """

    if b.check_game_over(b.game) == False:
        player_move()
        
    if b.check_game_over(b.game) == False:

        if difficulty == 1:
            bot.brain_dead()
        else:
            bot.noob()

if b.result == 'X' or b.result == 'O':
    print('---- Game Over ----')
    print(f'{b.result} Wins')
else: 
    print('---- Game Over - Draw ----')

    
b.show_board()
