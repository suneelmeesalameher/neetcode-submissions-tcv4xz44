class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row= len(board)
        col = len(board[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()

        def dfs(r, c):
            if r not in range(row) or c not in range(col) or board[r][c]!="O":
                return 
            board[r][c]="T"
            # if (r==0 or c==0 or r==row-1 or c==col-1) and board[r][c]=="O":
            #     return True
    
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            
            
        
        for r in range(row):
            for c in range(col):
                if (r==0 or c==0 or r==row-1 or c==col-1) and (board[r][c]=="O"):
                    dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c]="O"      
            

