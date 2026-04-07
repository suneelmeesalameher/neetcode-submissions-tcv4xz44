class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for x in prices:
            profit= x-minprice
            if maxprofit<profit:
                maxprofit=profit
            if x<minprice:
                minprice=x
        return maxprofit