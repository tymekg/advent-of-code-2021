lines = 0;
ones = {};
bits = 0;
boards = []
numbers = []

def readBoard(f):
    board = [0] * 5
    for y in range(5):
        line = f.readline()
        if not line:
            return None
        board[y] = list(map(int, line.split()))
    f.readline()
    return board

def board_won(board):
    for y in range(5):
        if sum(board[y]) == 0:
            return True
    for x in range(5):
        for y in range(5):
            if board[y][x] > 0:
                break
            if y == 4:
                return True
    return False

def board_score(board, draw):
    unmarked = sum(sum(board, []))
    return unmarked * draw

last_draw = 0
def find_winning_board():
    global last_draw
    for draw in numbers:
        for board in boards:
            for y in range (5):
                for x in range (5):
                    if board[y][x] == draw:
                        board[y][x] = 0
                        if board_won(board):
                            last_draw = draw
                            return board

def find_last_board():
    global last_draw
    complete_boards = []
    while len(boards) > len(complete_boards):
        for draw in numbers:
            for board in boards:
                if not board in complete_boards:
                    for y in range (5):
                        for x in range (5):
                            if board[y][x] == draw:
                                board[y][x] = 0
                                if board_won(board):
                                    last_draw = draw
                                    complete_boards.append(board)
                                    if len(boards) == len(complete_boards):
                                        return board

with open('day4/input.txt') as f:
    numbersLine = f.readline()
    numbers = list(map(int, numbersLine.split(',')))
    f.readline()
    while True:
        nextBoard = readBoard(f)
        if not nextBoard:
            break
        boards.append(nextBoard)
    best_board = find_last_board()
    print(board_score(best_board, last_draw))

