import board as b
import random as rd

def legal_moves():
    """
    Returns list of possible move indexes from current board state.
    """

    l_moves = []
    for i in range(0, len(b.game)):
        if b.game[i] == '*':
            l_moves.append(i)

    return l_moves

def bot_move():
    """
    Selects a random available position from legal moves and places 'O'.
    """
    available_moves = legal_moves()
    random_move = rd.choice(available_moves)
    b.game[random_move] = 'O'
