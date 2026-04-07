class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid), len(grid[0])
        q=deque()
        visit=set()

        def rangechecker(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])


        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visit:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist=0
        while q:
            for _ in range(len(q)):
                r,c= q.popleft()
                grid[r][c]=dist
                rangechecker(r-1,c)
                rangechecker(r+1,c)
                rangechecker(r,c-1)
                rangechecker(r,c+1)
            dist+=1
