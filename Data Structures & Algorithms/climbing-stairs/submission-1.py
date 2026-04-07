class Solution:
    def climbStairs(self, n: int) -> int:
        one=1
        two=1
        for x in range(0,n-1):
            x=one+two
            one, two=x, one
        return one