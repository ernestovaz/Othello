import random
import sys

sys.path.append("..")
from board import *

BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
MAX_SCORE = 1000
MIN_SCORE = -1000
DEPTH = 3


def eval_func(state : Board, color : str): #retorna qt. peças da cor
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


def max_val(state : Board, alfa: int, beta: int, depth: int, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna a avaliacao otimista
    node_value = MIN_SCORE #assumimos que a posicao tem pior valor possivel
    succ_list = successors(state,color)
    if not succ_list or depth == 0: #avalia nos-folha
        return eval_func(state, color)
        
    for s_state in succ_list:
        node_value = max(node_value, min_val(s_state, alfa, beta, depth - 1, color))
        alfa = max(alfa, node_value)
        if alfa >= beta: break #o oponente tem conhecidamente uma jogada melhor
        
    return node_value


def min_val(state : Board, alfa: int, beta: int, depth: int, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna a avaliacao pessimista (otimiza para o oponente)
    node_value = MAX_SCORE #assumimos que a posicao tem melhor valor possivel
    succ_list = successors(state,color)
    if not succ_list or depth == 0: #avalia nos-folha
        return eval_func(state, color)
        
    for s_state in succ_list:
        node_value = min(node_value, max_val(s_state, alfa, beta, depth - 1, color))
        beta = min(beta, node_value)
        if beta <= alfa: break
        
    return node_value


def alpha_beta_pruning(state : Board, depth: int, color: str): #obtem a lista de possiveis estados do tabuleiro e retorna o melhor avaliado

    succ_list = successors(state, color)
    if not succ_list:
        return (-1,-1)
    moves_dict = dict(zip(succ_list, state.legal_moves(color)))
    best_succ = max(succ_list, key= lambda x: min_val(x, MIN_SCORE, MAX_SCORE, depth - 1, color))
    return moves_dict[best_succ]
    
def make_move(the_board : Board, color : str):
	"""
	Returns an Othello move
	:param the_board: a board.Board object with the current game state
	:param color: a character indicating the color to make the move ('B' or 'W')
	:return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
	"""
	return alpha_beta_pruning(the_board, DEPTH, color)
    






