import random
import sys

sys.path.append("..")
from board import *

BLACK = 'B'
WHITE = 'W'
EMPTY = '.'


def eval_func(state : Board,color : str): #retorna qt. peças da cor
    s = str(state)
    value = 0
    for c in s:
        if c == color:
            value += 1
    return value


def successors(state: Board, color : str): #consulta a lista de possiveis movimentos e retorna lista de possiveis estados de tabuleiro
    succ_list = []
    moves = state.legal_moves(color)
    for m in moves:
        auxBoard = from_string(str(state))
        auxBoard.process_move(m, color)
        succ_list.append(auxBoard)
    return succ_list


def max_val(state : Board, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna o melhor avaliado
    succ_list = successors(state,color)
    if not succ_list:
        return eval_func(state, color)
    return max(min_val(s,color) for s in succ_list)


def min_val(state : Board, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna o pior avaliado
    succ_list = successors(state,color)
    if not succ_list:
        return eval_func(state, color)
    return min(max_val(s,color) for s in succ_list)


def minimax(state : Board, color: str):
    if state.is_terminal_state():
        return eval_func(state, color)
    succ_list = successors(state, color)
    if not succ_list:
        return (-1,-1)
    moves_dict = dict(zip(succ_list, state.legal_moves(color)))
    best_succ = max(succ_list, key= lambda x: min_val(x, color))
    return moves_dict[best_succ]

def make_move(the_board : Board, color : str):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    return minimax(the_board,color)
    






