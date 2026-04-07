class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxlength=1
        for num in numset:
            if num-1 in numset:
                length=1
                while num-length in numset:
                    length+=1
                maxlength=max(maxlength, length)
        return maxlength