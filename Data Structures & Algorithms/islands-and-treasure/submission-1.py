class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row= len(grid)
        col= len(grid[0])
        visit = set()
        q=deque()

        def rangechecker(r,c):
            if 0>r or 0>c or r>=row or c>=col or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c]==0 and (r,c) not in visit:
                    q.append([r,c])
                    visit.add((r,c))

        dist= 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                rangechecker(r+1,c)
                rangechecker(r,c+1)
                rangechecker(r-1,c)
                rangechecker(r,c-1)
            dist+=1

