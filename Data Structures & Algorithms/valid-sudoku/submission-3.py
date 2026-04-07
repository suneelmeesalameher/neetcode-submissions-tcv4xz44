class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)#9
        col=len(board[0])#9

        

        for r in board:
            mydir_r={}
            for num in r:
                if num.isdigit():
                    if num in mydir_r:
                        return False
                    mydir_r[num]=1
        

        for c in range(0,9):
            mydir_c={}
            for i in range(0,9):
                if board[i][c].isdigit():
                    if board[i][c] in mydir_c:
                        return False
                    mydir_c[board[i][c]]=1

        for x in [0,3,6]:
            for y in [0,3,6]:
                cubeset={}
                for r in range(x,x+3):
                    for c in range(y,y+3):
                        if board[r][c].isdigit():
                            if board[r][c] in cubeset:
                                return False
                            cubeset[board[r][c]]=1

        return True

                        

