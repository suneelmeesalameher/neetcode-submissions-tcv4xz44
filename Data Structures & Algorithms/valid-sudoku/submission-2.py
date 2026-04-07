class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowset=set()
            for num in row:
                if num in rowset:
                    return False
                if num !=".":
                    rowset.add(num)
        
        for col in range(9):
            colset=set()
            for i in range(9):
                if board[i][col] in colset:
                    return False
                if board[i][col] !=".":
                    colset.add(board[i][col])
        
        for square in range(9):
            squareset=set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square %3)*3 + j
                    if board[row][col] in squareset:
                        return False
                    if board[row][col] !=".":
                        squareset.add(board[row][col])
        return True