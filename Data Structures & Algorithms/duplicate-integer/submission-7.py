class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydir={}
        for num in nums:
            if num in mydir:
                return True
            else:
                mydir[num]=1
        return False
