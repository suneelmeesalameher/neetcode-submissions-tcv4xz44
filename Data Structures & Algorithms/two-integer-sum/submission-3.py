class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydir={}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in mydir:
                return [mydir[complement],i]
            mydir[num]=i
        return []