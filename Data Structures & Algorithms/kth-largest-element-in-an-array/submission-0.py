class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(0,len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        
        for i in range(0,k):
            ans=heapq.heappop(nums)
        return -ans      