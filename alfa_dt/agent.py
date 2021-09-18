import random
import sys
from time import time

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


def max_val(state : Board, alfa: int, beta: int, T: float, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna a avaliacao otimista
    ti = time()
    if time() - ti >= T: 
        return MAX_SCORE
    node_value = MIN_SCORE #assumimos que a posicao tem pior valor possivel
    succ_list = successors(state,color)
    if not succ_list: #avalia nos-folha
        return eval_func(state, color)

    succ_n = len(succ_list)
    for s_state in succ_list:
        if time() - ti >= T: break
        node_value = max(node_value, min_val(s_state, alfa, beta, T/succ_n, color))
        alfa = max(alfa, node_value)
        if alfa >= beta: break #o oponente tem conhecidamente uma jogada melhor
        
    return node_value


def min_val(state : Board, alfa: int, beta: int, T: int, color : str): #obtem a lista de possiveis estados de tabuleiro e retorna a avaliacao pessimista (otimiza para o oponente)
    ti = time()
    if time() - ti >= T: 
        return MIN_SCORE
    node_value = MAX_SCORE #assumimos que a posicao tem melhor valor possivel
    succ_list = successors(state,color)
    if not succ_list: #avalia nos-folha
        return eval_func(state, color)
       
    succ_n = len(succ_list)
    for s_state in succ_list:
        if time() - ti >= T: break
        node_value = min(node_value, max_val(s_state, alfa, beta, T/succ_n, color))
        beta = min(beta, node_value)
        if beta <= alfa: break
        
    return node_value


def alpha_beta_pruning(state : Board, T: float, color: str): #obtem a lista de possiveis estados do tabuleiro e retorna o melhor avaliado
    ti = time()
    succ_list = successors(state, color)
    if not succ_list:
        return (-1,-1)

    moves = state.legal_moves(color)
    succ_n = len(succ_list)
    node_value = MIN_SCORE 
    best_id = 0

    for i,s in enumerate(succ_list): 
        if time() - ti >= T: break
        min_succ = min_val(s,MIN_SCORE,MAX_SCORE,T/succ_n,color)
        if min_succ > node_value:
            best_id = i
            node_value = min_succ

    return moves[best_id]
    
def make_move(the_board : Board, color : str):
	"""
	Returns an Othello move
	:param the_board: a board.Board object with the current game state
	:param color: a character indicating the color to make the move ('B' or 'W')
	:return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
	"""
	return alpha_beta_pruning(the_board, 4.99, color)
    






