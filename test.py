import unittest

def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    
    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [board[r][c] for r in range(row, row+3) for c in range(col, col+3)]
            if not is_valid_set(subgrid):
                return False
    
    return True

def is_valid_set(nums):
    seen = set()
    for num in nums:
        if num != 0 and num in seen:
            return False
        seen.add(num)
    return True

class TestSudoku(unittest.TestCase):
    # def test_valid_sudoku(self):
    #     board = [
    #         [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #         [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #         [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #         [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #         [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #         [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #         [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #         [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #         [0, 0, 0, 0, 8, 0, 0, 7, 9]
    #     ]
    #     self.assertTrue(is_valid_sudoku(board))
    
            # new_sudokus.append(sudokus[i])
        
    def test_valid_sudoku(self):
        board=[["" for i in range(9)]for j in range(9)]
        file=open("sudokus\sudokus_expert.txt","r")
        sudokus=file.readlines()
        # print(sudokus)
        # new_sudokus=[]
        for i in range(0,len(sudokus),2):
            sudoku=sudokus[i].strip("\n")
            print(sudoku)
            print(len(sudoku))
            for j in range(9):
                for k in range(9):
                    if sudoku[j+k]!=".":
                        board[j][k]=int(sudoku[j+k])
                    else:
                        board[j][k]=0
                #if sudokus[i] in ("1","2","3","4","5","6","7","8","9") else 0
            # print(board)
            self.assertTrue(is_valid_sudoku(board))


    def test_invalid_sudoku(self):
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 8]  # Invalid duplicate '8' in the last cell
        ]
        self.assertFalse(is_valid_sudoku(board))



if __name__ == '__main__':
    unittest.main()
    