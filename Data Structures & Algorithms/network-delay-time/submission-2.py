class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minheap =[(0,k)]
        visit=set()
    
        t=0
        while minheap:
            w1,v1=heapq.heappop(minheap)
            if v1 in visit:
                continue
            t=max(t,w1)
            visit.add(v1)
            for v2,w2 in edges[v1]:
                heapq.heappush(minheap, (w2+w1, v2))
        
        return t if len(visit)==n else -1
            