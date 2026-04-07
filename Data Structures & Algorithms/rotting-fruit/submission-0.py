class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        visit=set()
        q=deque()
        fresh =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2 and (r,c) not in visit:
                    q.append([r,c])
                    visit.add((r,c))
        

        def rangechecker(r,c):
            nonlocal fresh
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
            fresh-=1

        rotten=2
        minute=0
        while q and fresh:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=rotten
                rangechecker(r-1,c)
                rangechecker(r+1,c)
                rangechecker(r,c-1)
                rangechecker(r,c+1)
            minute+=1
        return minute if fresh==0 else -1


