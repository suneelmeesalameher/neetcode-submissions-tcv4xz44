class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))
        post=1
        for i in range(1,len(nums)):
            res[i]=post*nums[i-1]
            post=res[i]
        
        pre=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=pre*res[i]
            pre=nums[i]*pre
        
        return res

        
