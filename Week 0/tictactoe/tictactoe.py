"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

globalList = set()
globalActions = []
tmpList = []


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


'''def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]'''


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xNum = 0
    yNum = 0

    for i in range(len(board)):

        for j in range(len(board[i])):

            if board[i][j] == "X":
                xNum += 1
            elif board[i][j] == "O":
                yNum += 1

    if xNum < yNum:
        return X
    elif yNum < xNum:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availActions = set()

    for i in range(len(board)):

        for j in range(len(board[i])):

            if board[i][j] == EMPTY:
                availActions.add((i, j))

    return availActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.copy(board)

    playerTurn = player(board)

    boardCopy[action[0]][action[1]] = playerTurn

    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):

        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return X
        elif board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return O
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return O
        elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return X

    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return O
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return X
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return X
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    availActions = list(actions(board=board))

    valuesList = []
    valueActions = []

    for action in availActions:
        tmpBoard = copy.deepcopy(board)
        valueActions.append(action)
        getMaxVal(result(tmpBoard, action))
        print(globalList)
        # i want the minimum solution
        tmp = list(globalList)
        valuesList.append(max(tmp))
        # i need the index of minimum val

        #clear the lists
        globalList.clear()
        globalActions.clear()
    minIndex = getMin(valuesList)

    print(valuesList)
    print(valueActions)
    print(minIndex)
    return valueActions[minIndex]


def getMin(arr):
    minimum = 19198
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index = i
    return index


def getMaxVal(board):
    if terminal(board):
        res = utility(board)
        print (res)
        globalList.add(res)
        return res

    availActions = list(actions(board=board))
    for action in availActions:
        newBoard = copy.deepcopy(board)
        newBoard = result(newBoard, action)

        getMaxVal(newBoard)


if __name__ == "__main__":
    board = initial_state()

    # print(player(board=board))

    availActions = list(actions(board=board))

    # for (i, j) in availActions:
    # print(f"{i} : {j}")

    # print(result(board, availActions[2]))

    # print(terminal(board))

    minimax(board)
