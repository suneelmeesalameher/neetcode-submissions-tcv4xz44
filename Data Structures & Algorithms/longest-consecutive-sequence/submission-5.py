class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum=set(nums)
        count=0
        for x in nums:
            if x-1 not in setnum:
                length=1
                while x+length in setnum:
                    length=length+1
                if count<length:
                    count=length
        return count
