class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #visited=set()
        if board is None:
            return False
        row= len(board)
        col= len(board[0])
        def dfs(r, c, i):
            if r not in range(row) or c not in range(col) or board[r][c]!=word[i] or board[r][c] =='#':
                return False
            if board[r][c] == word[i]:
                if len(word)-1== i:
                    return True
                else:
                    temp=board[r][c]
                    board[r][c]='#'
                    found= dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
                    if found:
                        return True
                    else:
                        board[r][c]=temp


        
        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True
        
        return False 