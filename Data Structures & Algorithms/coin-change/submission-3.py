class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        if amount==0:
            return dp[0]
        #for coin in coins:
        #    dp[coin]=1
        
        for i in range(0,amount+1):
            for c in coins:
                if c<=i:
                    dp[i]=min(dp[i],dp[i-c]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1