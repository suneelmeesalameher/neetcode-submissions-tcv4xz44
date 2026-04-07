class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        sum_n= (n*(n+1))/2
        sumi=0
        for x in nums:
            sumi=sumi+x
        return int(sum_n-sumi)
        