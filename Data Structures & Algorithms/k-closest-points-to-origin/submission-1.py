class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        arr=[]
        heapq.heapify(arr)
        for point in points:
            x,y=point[0],point[1]
            dist=(math.sqrt((x)**2 + (y)**2))
            
        
            heapq.heappush(arr,(dist, [x,y]))
        

        for i in range(0,k):
            _,point=heapq.heappop(arr)
            ans.append(point)

        return ans