import random
import sys

sys.path.append("..")
from board import *

BLACK = 'B'
WHITE = 'W'
EMPTY = '.'


def eval_func(stateStr : str,color : str): #retorna qt. peças da cor
    value = 0
    for i in stateStr:
        if i == color:
            value += 1
    return value

def successor_states(state: Board, color : str):
    succ_list = []
    moves = state.legal_moves(color)
    for m in moves:
        auxBoard = from_string(str(state))
        auxBoard.process_move(m, color)
        succ_list.append(auxBoard)
    return succ_list


#def max_val(state : Board, color : str):
#    if state.is_terminal_state():
#        return eval_func(state, color)
#    v = None
#    for succ in 
#
#def minimax(state : Board, color: str):
#    return None

def make_move(the_board : Board, color : str):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    return None
    






