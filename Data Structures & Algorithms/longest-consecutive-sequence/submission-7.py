class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for num in nums:
            if num-1 not in numset:
                #its the first element of a sequence
                length=1
                x=num
                while x+1 in numset:
                    x=x+1
                    length+=1
                longest=max(longest, length)
        return longest