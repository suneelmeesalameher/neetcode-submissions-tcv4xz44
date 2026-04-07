class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        #directions=[[1,0],[0,1],[-1,0],[0,-1]]
        maxarea=0
        visited=set()

        def dfs(r,c):
            if 0>r or r>=row or 0>c or c>=col or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r, c-1)
            
            

        
        for r in range(0,row):
            for c in range(0,col):
                if grid[r][c] ==1:
                    area=dfs(r,c)
                    maxarea=max(area, maxarea)
        
        return maxarea


        
