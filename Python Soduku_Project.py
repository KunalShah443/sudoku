import tkinter as tk
from tkinter import messagebox

# Define the Sudoku solver functions (from the previous example)
def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Create the GUI
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0]*9 for _ in range(9)]
        self.entries = [[None]*9 for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(frame, width=2, font=('Arial', 18), borderwidth=2, relief="ridge", justify="center")
                self.entries[i][j].grid(row=i, column=j)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.pack()

    def solve_puzzle(self):
        self.read_board()
        if solve(self.board):
            self.display_board()
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle")

    def read_board(self):
        for i in range(9):
            for j in range(9):
                try:
                    val = int(self.entries[i][j].get())
                    self.board[i][j] = val if 1 <= val <= 9 else 0
                except ValueError:
                    self.board[i][j] = 0

    def display_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()