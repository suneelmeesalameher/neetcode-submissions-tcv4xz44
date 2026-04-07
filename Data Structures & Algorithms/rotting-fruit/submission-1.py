class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row= len(grid)
        col= len(grid[0])
        time=0
        #directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()
        q = deque()
        fresh=0
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
                    fresh+=1

        def rangechecker(r,c):
            nonlocal fresh
            if r not in range(row) or c not in range(col) or (r,c) in visited or grid[r][c]==0:
                return 
            fresh= fresh -1
            visited.add((r,c))
            q.append([r,c])

        for r in range(row):
            for c in range(col):
                if grid[r][c] ==2 and (r,c) not in visited:
                    visited.add((r,c))
                    q.append([r,c])
        time=0
        while q and fresh:
            for i in range(len(q)):
                dr,dc = q.popleft()
                grid[dr][dc]=2
                rangechecker(dr+1,dc)
                rangechecker(dr-1,dc)
                rangechecker(dr,dc+1)
                rangechecker(dr,dc-1)
            time+=1

        
        return time if fresh==0 else -1