class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        i=len(nums)-2
        while i>-1:
            if i+2 < len(nums) and i+3 <len(nums):
                nums[i]+=max(nums[i+2], nums[i+3])
            i-=1
        return max(nums[0],nums[1])