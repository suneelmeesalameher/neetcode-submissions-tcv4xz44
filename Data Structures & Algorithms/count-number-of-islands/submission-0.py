class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        visit=set()
        island=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                if 0<r+1<rows and grid[r+1][c] =="1" and (r+1,c) not in visit :
                    q.append((r+1,c))
                    visit.add((r+1,c))
                if 0<=r-1<rows and grid[r-1][c] =="1" and (r-1,c) not in visit:
                    q.append((r-1,c))
                    visit.add((r-1,c))
                if 0<=c-1<cols and grid[r][c-1]=="1" and (r,c-1) not in visit:
                    q.append((r,c-1))
                    visit.add((r,c-1))
                if 0<c+1<cols and grid[r][c+1]=="1" and (r,c+1) not in visit:
                    q.append((r,c+1))
                    visit.add((r,c+1))
                
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island