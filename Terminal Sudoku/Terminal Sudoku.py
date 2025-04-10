import random

# Function to print the Sudoku Board
def print_board(board):
    for row_index in range(9):
        # Prints the Horizontal lines
        if row_index % 3 == 0 and row_index != 0:
            print("- - - - - - - - - - -")
        for col_index in range(9):
            # Prints the Vertical Lines
            if col_index % 3 == 0 and col_index != 0:
                print("|", end=" ")
            # Prints a "." if the cell is empty
            if board[row_index][col_index] == 0:
                print(".", end=" ") 
            else:
                # Prints the number on the board
                print(board[row_index][col_index], end=" ")
        print()  

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

# Main function to play Sudoku
def play_sudoku():
    board = generate_board()
    original_board = [row[:] for row in board]
    while True:
        print_board(board)
        print("")
        action = input("Enter 'row col num' to insert or 'solve' to solve: ")

        # Checks if the user wants to solve
        if action == "solve":
            solve_sudoku(original_board)
            print("Solved Sudoku:")
            print_board(original_board)
            break
        
        # Checks if input is valid and inputs it into the board if so, returns error if not
        try:
            row, col, num = map(int, action.split()) 
            if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
                if board[row - 1][col - 1] == 0 and is_valid_move(board, row, col, num):
                    board[row - 1][col - 1] = num 
                else:
                    # Returns error
                    print("Invalid move! Try again.")
            else:
                # Returns error
                print("Invalid input! Use numbers between 1-9 for 'row', 'col' and 'num'.")
        except ValueError:
            # Returns error
            print("Invalid input format! Use 'row col num' or 'solve'.")

# Starts a Sudoku Game
play_sudoku()