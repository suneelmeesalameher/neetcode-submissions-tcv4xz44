class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        Parent=list(range(len(edges)+1))
        size=[1]*(len(edges)+1)

        def find(node):
            if Parent[node]!=node:
                Parent[node]=find(Parent[node])
            return Parent[node]
        
        def union(u, v):
            pu= find(u)
            pv= find(v)

            if pu==pv:
                return False
            
            if size[pu]<size[pv]:
                pu,pv=pv,pu

            size[pu]+=size[pv]
            Parent[pv] = pu
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]