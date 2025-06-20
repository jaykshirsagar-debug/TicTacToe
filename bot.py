"""
Filename:         bot.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page handles the bots move in the Tic-tac-toe game.
"""

import board as b
import random as rd

def copy_board(board):
    return board.copy()

def legal_moves(board):
    """
    Returns a list of indices where moves are possible (empty spots).
    """
    l_moves = []
    for i in range(len(board)):
        if board[i] == '*':
            l_moves.append(i)
    return l_moves

class Bots:
    def __init__(self):
        pass


    def brain_dead(self):
        """
        Brain Dead bot that makes random moves
        """
        valid_move = False
        while valid_move == False:
            random_move = rd.randint(1,9)
            if b.game[random_move - 1] == '*':
                b.game[random_move - 1] = 'O'
                b.show_board()
                valid_move = True


    """
Filename:         bot.py
Author:           Jay Kshirsagar
Date Created:     06/06/2025
Description:      This page handles the bots move in the Tic-tac-toe game.
"""

import board as b
import random as rd

def copy_board(board):
    return board.copy()

def legal_moves(board):
    """
    Returns a list of indices where moves are possible (empty spots).
    """
    l_moves = []
    for i in range(len(board)):
        if board[i] == '*':
            l_moves.append(i)
    return l_moves

class Bots:
    
    def __init__(self):
        pass

    def brain_dead(self):
        """
        Brain Dead bot that makes random moves
        """
        valid_move = False
        while valid_move == False:
            random_move = rd.randint(1,9)
            if b.game[random_move - 1] == '*':
                b.game[random_move - 1] = 'O'
                b.show_board()
                valid_move = True

    def noob(self):
        """
        Noob bot that makes random moves, except when it can win immediately or needs to block.
        """
        board = copy_board(b.game)
        l_moves = legal_moves(board)
        
        # First check if bot can win
        for move in l_moves:
            board_copy = copy_board(board)
            board_copy[move] = 'O'
            
            if b.check_win_condition(board_copy) == 'O':
                b.game[move] = 'O'
                b.show_board()
                return
        
        # Then check if bot needs to block player's win
        for move in l_moves:
            board_copy = copy_board(board)
            board_copy[move] = 'X'
            
            if b.check_win_condition(board_copy) == 'X':
                b.game[move] = 'O'
                b.show_board()
                return
        
        # Otherwise make random move
        random_move = rd.choice(l_moves)
        b.game[random_move] = 'O'
        b.show_board()

