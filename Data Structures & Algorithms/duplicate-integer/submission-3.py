class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dir={}
        for x in nums:
            if x in my_dir:
                return True
            else:
                my_dir[x]=1
        return False 
         