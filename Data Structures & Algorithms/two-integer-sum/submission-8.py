class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydir={}
        for i, num in enumerate(nums):
            mydir[num]= i
            if(target- num) != num and (target- num) in mydir:
                return [mydir[target-num], mydir[num]]
        return None
        

            