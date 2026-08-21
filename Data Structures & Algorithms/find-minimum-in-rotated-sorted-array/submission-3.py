class Solution:
    def findMin(self, nums: List[int]) -> int:
        least=float('inf')
        left=0
        right=len(nums)-1

        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                #the left side is prolly sorted
                left=mid+1
            elif nums[left]>nums[mid]:
                #the right side is prolly sorted
                right=mid
        return nums[left]
        






















        # if len(nums)==1:
        #     return nums[0]
        # leftptr=0
        # rightptr=len(nums)-1
        # while leftptr<rightptr:
        #     mid=(leftptr+rightptr)//2
        #     if nums[mid]>nums[rightptr]:
        #         #ans=min(ans,nums[rightptr])
        #         leftptr=mid+1
        #     elif nums[mid]< nums[rightptr]:
        #         #ans=min(ans,nums[leftptr])
        #         rightptr=mid
        # return nums[leftptr] 