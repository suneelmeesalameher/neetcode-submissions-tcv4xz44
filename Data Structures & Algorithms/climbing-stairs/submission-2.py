class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2

        comb=[0]*(n)
        comb[0]=1
        comb[1]=2

        for i in range(2,n):
            comb[i]=comb[i-1]+comb[i-2]
        return comb[n-1]