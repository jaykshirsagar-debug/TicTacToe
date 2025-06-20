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
result = ''

def show_board():
    """Displays the current state of the Tic-Tac-Toe board in a grid format."""
    print(f'{game[0]}  {game[1]}  {game[2]}')
    print(f'{game[3]}  {game[4]}  {game[5]}')
    print(f'{game[6]}  {game[7]}  {game[8]}')

def check_win_condition(board):
    """Checks if there's a win condition on the board without side effects.
    Returns:
        str: 'X' if X wins, 'O' if O wins, 'draw' if draw, None if game continues
    """
    # Check all winning combinations
    # Inspired by Claude AI but I understand the concept:)
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '*':
            return board[combo[0]]
    
    # Check for draw
    if '*' not in board:
        return 'draw'
    
    return None

def check_game_over(board):
    """Checks if game is over by win condition or draw.
    Returns:
        bool: True if game is over, False if game continues
    """
    global game_over
    global num_moves
    global result
    
    # The game requires a minimum of 5 moves to be over
    # Only starts to check win after 5 or more moves
    if num_moves >= 5:
        result = check_win_condition(board)
        
        if result == 'X' or result == 'O' or result == 'draw':
        
            game_over = True
        
    else:
        num_moves += 1
    
    return game_over