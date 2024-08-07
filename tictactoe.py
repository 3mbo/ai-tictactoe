"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == X:
                xs += 1
            if board[i][j] == O:
                os += 1
    if xs > os:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set1 = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] is None:
                set1.add((i, j))
    return set1


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    newboard = copy.deepcopy(board)
    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if len(set([board[i][j] for j in range(3)])) == 1 and board[i][0] != None:
            return board[i][0]

    for j in range(3):
        if len(set([i[j] for i in board])) == 1 and board[0][j] != None:
            return board[0][j]

    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != None:
        return board[0][0]

    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    if actions(board) == set():
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def maxV(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, minV(result(board, action)))
        return v

    def minV(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, maxV(result(board, action)))
        return v

    if player(board) == X:
        bestV = -math.inf
        for action in actions(board):
            if minV(result(board, action)) > bestV:
                bestV = minV(result(board, action))
                best = action
        return best
    else:
        bestV = math.inf
        for action in actions(board):
            if maxV(result(board, action)) < bestV:
                bestV = maxV(result(board, action))
                best = action
        return best
