class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1=0
        for num in nums:
            x1=x1^num
        return x1