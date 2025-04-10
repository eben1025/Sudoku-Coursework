import random

# Function to check if a move is valid
def is_valid_move(board, row, col, num):
    # Zero Based Indexing
    row -= 1
    col -= 1
    
    # Checks if the number exists in its row
    if num in board[row]:
        return False

    # Checks if the number exists in its column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Checks if number exists in its 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Function that finds the first empty cell on the board
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Solves the sudoku board using backtracking
def solve_sudoku(board):
    board_copy = [row[:] for row in board]  
    empty_cell = find_empty_cell(board_copy)
    if not empty_cell:
        return True  

    row, col = empty_cell
    for num in range(1, 10):  
        if is_valid_move(board_copy, row + 1, col + 1, num):
            board_copy[row][col] = num  
            if solve_sudoku(board_copy): 
                board[:] = board_copy 
                return True
            board_copy[row][col] = 0 
    return False

# Function that randomly generates a Sudoku board
def generate_board():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(random.randint(10, 20)):
        row, col = random.randint(1, 9), random.randint(1, 9)
        num = random.randint(1, 9)
        while not is_valid_move(board, row, col, num) or board[row - 1][col - 1] != 0:
            row, col = random.randint(1, 9), random.randint(1, 9)
            num = random.randint(1, 9)
        board[row - 1][col - 1] = num
    return board