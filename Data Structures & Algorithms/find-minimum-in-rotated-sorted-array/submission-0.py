class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        leftptr=0
        rightptr=len(nums)-1
        while leftptr<rightptr:
            mid=(leftptr+rightptr)//2
            if nums[mid]>nums[rightptr]:
                #ans=min(ans,nums[rightptr])
                leftptr=mid+1
            elif nums[mid]< nums[rightptr]:
                #ans=min(ans,nums[leftptr])
                rightptr=mid
        return nums[leftptr] 