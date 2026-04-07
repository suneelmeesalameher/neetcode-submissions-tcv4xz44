class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydir ={}

        for i in range(len(nums)):
            if target-nums[i] in mydir and i!= mydir[target-nums[i]]:
                return [mydir[target-nums[i]], i]
            else:
                mydir[nums[i]]=i
                
        return None
