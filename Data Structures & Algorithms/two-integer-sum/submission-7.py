class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydir={}

        for i, num in enumerate(nums):
            if target - num in mydir and i!= mydir[target-num]:
                return[mydir[target-num], i]
            else:
                mydir[num]=i
        
