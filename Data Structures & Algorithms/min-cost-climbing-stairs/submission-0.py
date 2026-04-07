class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #minimumfinal=float('inf')
        cost.append(0)
        i=len(cost)-2
        while i>-1:
            if cost[i+1] and cost[i+2]:
                cost[i]=min(cost[i]+cost[i+1], cost[i]+cost[i+2])
            #minimumfinal=min(minimumfinal, cost[i])
            i-=1
        return min(cost[0], cost[1])