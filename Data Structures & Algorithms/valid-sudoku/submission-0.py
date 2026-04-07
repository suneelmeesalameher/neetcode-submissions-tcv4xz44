class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            rowset=set()
            for x in row:
                if x.isdigit():
                    if x in rowset:
                        return False
                    else:
                        if int(x)>0 and int(x)<10:
                            rowset.add(x)
                        else:
                            return False

        for col in range(0,9):
            colset=set()
            for row in range(0,9):
                y=board[row][col]
                if board[row][col].isdigit():
                    if board[row][col] in colset:
                        return False
                    else:
                        if int(board[row][col]) >0 and int(board[row][col])<10:
                            colset.add(board[row][col])
                        else:
                            return False
        
        for x in [0,3,6]:
            for y in [0,3,6]:
                cubeset=set()
                for row in range(x,x+3):
                    for col in range(y,y+3):
                        if board[row][col].isdigit():
                            if board[row][col] in cubeset:
                                return False
                            else:
                                if int(board[row][col])>0 and int(board[row][col])<10:
                                    cubeset.add(board[row][col])
                                else:
                                    return False
        return True
