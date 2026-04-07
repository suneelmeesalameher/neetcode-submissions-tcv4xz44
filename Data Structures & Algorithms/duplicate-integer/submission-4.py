class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydir={}
        for i in range(len(nums)):
            if nums[i] in mydir:
                return True
            mydir[nums[i]]=1
        return False