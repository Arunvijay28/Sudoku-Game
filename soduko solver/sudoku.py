#PYTHON APPLICATION PROGRAM
#PYTHON SUDOKU SOLVER PROGRAM

#GUI.PY
from tkinter import *

from so import *

root = Tk()
root.title("sudoku solver")
root.geometry("324x550")

label = Label(root, text="fill in the numbers and click solve")
label.grid(row=0, column=1, columnspan=10)

#error message
errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

#solved message
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

#creating a dictionary to store the elements of the cell
cells = {}

def validatenumber(P):
    out = (P.isdigit() or P=="") and len(P)<2
    return out

#regestering the function
reg = root.register(validatenumber)

#writing a function to draw a 3x3 grid
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

#writing a fuction to draw a 9x9 grid
def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

#writing a function to get input from the user
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(0, 9, 3):
            cell = cells[(row, col)]
            cell.delete(0, "end")

def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

#code for buttons
#button 1
btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

#button 2
btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)

def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows-2][col-1])
        solvedLabel.configure(text="Sudoku Solved")
    else:
        errLabel.configure(text="No solution exists for this sudoku")

draw9x9Grid()
root.mainloop()


