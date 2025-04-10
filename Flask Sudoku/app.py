from flask import Flask, request, redirect, render_template
from sudoku_logic.helpers import is_valid_move, generate_board, find_empty_cell, solve_sudoku

app = Flask(__name__)

# Generats the sudoku board with random values
board = generate_board()

# Home route that shows the current state of the board
@app.route("/")
def index():
    # Gets any error messages 
    error_message = request.args.get("error", "")
    # Rendes the HTML page and passes the board and any error messages
    return render_template("index.html", board=board, error_message=error_message)

# Route that handles any user inputs
@app.route("/play", methods=["POST"])
def play():
    try:
        # Extracts the row, column and number from the form and subtracts 1 for zero based indexing
        row = int(request.form["row"]) - 1
        col = int(request.form["col"]) - 1
        num = int(request.form["num"])

        # Checks if selected cell is empty and move is valid
        if board[row][col] == 0 and is_valid_move(board, row + 1, col + 1, num):
            # Places the number on the board
            board[row][col] = num
        else:
            # Returns an error
            return redirect("/?error=Invalid+Move")
    except:
        # Returns an error
        return redirect("/?error=Invalid+Input")
    return redirect("/")

# Route to solve the board
@app.route("/solve")
def solve():
    solve_sudoku(board)
    return redirect("/")

# Route to start a new game
@app.route("/reset")
def reset():
    global board
    board = generate_board()
    return redirect("/")

# Starts the flask server
app.run(debug=True)