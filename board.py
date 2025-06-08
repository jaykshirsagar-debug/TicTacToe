"""
Filename:         board.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page displays the state of board after either the player or bot moves, and after the game ends.
"""

game = ['*','*','*',
        '*','*','*',
        '*','*','*',]

num_moves = 0
game_over = False

def show_board():
    """Displays the current state of the Tic-Tac-Toe board in a grid format."""
    print(f'{game[0]}  {game[1]}  {game[2]}')
    print(f'{game[3]}  {game[4]}  {game[5]}')
    print(f'{game[6]}  {game[7]}  {game[8]}')

def check_game_over(board):
    """Checks if game is over by win condition or draw.
    Returns:
        bool: True if game is over, False if game continues
    """
    global game_over
    global num_moves
    #The game requires a minimum of 5 moves to be over
    #Only starts to check win after 5 or more moves
    if num_moves >= 5:

        if (board[0] == board[1] == board[2] == 'X') or (board[0] == board[1] == board[2] == 'O'):
            print('---- Game Over ----')
            print(f'{board[0]} Wins')
            game_over = True
        elif (board[2] == board[5] == board[8] == 'X') or (board[2] == board[5] == board[8] == 'O'):
            print('---- Game Over ----')
            print(f'{board[2]} Wins')
            game_over = True
        elif (board[6] == board[7] == board[8] == 'X') or (board[6] == board[7] == board[8] == 'O'):
            print('---- Game Over ----')
            print(f'{board[6]} Wins')
            game_over = True
        elif (board[0] == board[3] == board[6] == 'X') or (board[0] == board[3] == board[6] == 'O'):
            print('---- Game Over ----')
            print(f'{board[0]} Wins')
            game_over = True
        elif (board[0] == board[4] == board[8] == 'X') or (board[0] == board[4] == board[8] == 'O'):
            print('---- Game Over ----')
            print(f'{board[0]} Wins')
            game_over = True
        elif (board[2] == board[4] == board[6] == 'X') or (board[2] == board[4] == board[6] == 'O'):
            print('---- Game Over ----')
            print(f'{board[2]} Wins')
            game_over = True
        elif (board[3] == board[4] == board[5] == 'X') or (board[3] == board[4] == board[5] == 'O'):
            print('---- Game Over ----')
            print(f'{board[3]} Wins')
            game_over = True
        elif (board[1] == board[4] == board[7] == 'X') or (board[1] == board[4] == board[7] == 'O'):
            print('---- Game Over ----')
            print(f'{board[1]} Wins')
            game_over = True

        if '*' not in board and game_over == False:
            print('---- Game Over - Draw ----')
            game_over = True
    else:
        num_moves += 1
    
    return game_over