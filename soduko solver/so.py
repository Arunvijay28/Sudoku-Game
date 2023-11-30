N = 9

# Function to check if it's safe to put a number in a cell
def isSafe(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    # Checking if the same number exists in the same row or column
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True

# Sudoku solve function
def solveSudoku(sudoku, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)
    for num in range(1, N+1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solveSudoku(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0
    return False

# Checking if sudoku is solvable
def solver(sudoku):
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        return "no"
