import random
import sys
import time

sys.path.append("..")
import board

BLACK = 'B'
WHITE = 'W'
EMPTY = '.'


def eval_func(state : str,color : str): #retorna qt. peças da cor
    value = 0
    for i in range(7):
        for j in range(7):
            if state[i][j] == color:
                value += 1
    return value

def make_move(the_board : board, color : str):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    






