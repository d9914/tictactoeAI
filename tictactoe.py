"""
Tic Tac Toe Player
"""
import copy
import math

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
    if terminal(board) == True:
        return True

    elif board == EMPTY:
        return X
    else:
        x_count = 0
        o_count = 0
        for row in board:
            for value in row:
                if value == 'X':
                    x_count += 1
                elif value == 'O':
                    o_count += 1
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == True:
        return True

    moves = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == None:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = copy.deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == X:
                return X
            elif row[0] == O:
                return O

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == X:
                return X
            elif board[0][col] == O:
                return O

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        score = -math.inf
        action_to_take = None

        for action in actions(board):
            min_val = Min_Value(result(board, action))

            if min_val > score:
                score = min_val
                action_to_take = action

        return action_to_take

    elif player(board) == O:
        score = math.inf
        action_to_take = None

        for action in actions(board):
            max_val = Max_Value(result(board, action))

            if max_val < score:
                score = max_val
                action_to_take = action

        return action_to_take


def Min_Value(board):
    v = float("inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, Max_Value(result(board, action)))
    return v


def Max_Value(board):
    v = -float("inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))
    return v
