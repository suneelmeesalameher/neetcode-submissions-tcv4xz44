import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        heap=[] # -value, r
        l=0
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            if r>=k-1:
                while heap[0][1] <= r - k:
                    heapq.heappop(heap)
                #val, right = heapq.heappop(heap)
                ans.append(- heap[0][0])
        return ans
