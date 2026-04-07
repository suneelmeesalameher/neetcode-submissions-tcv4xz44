class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydir={}
        for i, num in enumerate(nums):
            if target-num in mydir:
                return [mydir[target-num], i]
            mydir[num]=i
                

            