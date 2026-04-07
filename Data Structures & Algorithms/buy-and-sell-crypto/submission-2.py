class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue= prices[0]
        profit=0
        for price in prices:
            if minvalue>price:
                minvalue=price
            if profit < price - minvalue:
                profit = price - minvalue
        return profit