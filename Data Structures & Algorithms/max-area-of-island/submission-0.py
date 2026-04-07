class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        maxarea=0
        if grid is None:
            return maxarea
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c=q.popleft()
                dirs=[[-1,0],[1,0],[0,-1],[0,1]]
                for dirr, dirc in dirs:
                    #r,c=r+dirr,c+dirc
                    if r+dirr in range(rows) and c+dirc in range(cols) and grid[r+dirr][c+dirc]==1 and (r+dirr,c+dirc) not in visit:
                        q.append((r+dirr,c+dirc))
                        visit.add((r+dirr,c+dirc))



        for r in range(rows):
            for c in range(cols):
                setlength=len(visit)
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)
                    newlength=len(visit)- setlength
                    maxarea=max(maxarea, newlength)
        return maxarea
