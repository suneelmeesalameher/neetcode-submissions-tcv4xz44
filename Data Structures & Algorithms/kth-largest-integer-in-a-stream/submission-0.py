class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        #for i in range(len(self.nums)):
        #    self.nums[i]=-self.nums[i]
        #self.queue=deque([self.nums])
        self.k=k
        heapq.heapify(self.nums)

        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        
