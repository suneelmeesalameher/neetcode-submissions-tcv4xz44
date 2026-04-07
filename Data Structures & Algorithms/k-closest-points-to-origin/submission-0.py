class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        min_heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (distance, [x, y]))

        for i in range(0, k):
            _, point=heapq.heappop(min_heap)
            ans.append(point)
        
        return ans