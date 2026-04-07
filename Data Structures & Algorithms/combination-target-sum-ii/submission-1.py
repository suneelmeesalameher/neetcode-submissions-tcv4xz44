class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sublist=[]
        res=[]

        def dfs(i, total, target):
            if target==total:
                res.append(sublist.copy())
                return
            
            if target<total or i>=len(candidates):
                return
            sublist.append(candidates[i])
            dfs(i+1, total+candidates[i],target)
            sublist.pop()
            
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total, target)



        dfs(0,0, target)
        return res