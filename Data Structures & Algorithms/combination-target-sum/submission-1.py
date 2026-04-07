class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sublist=[]
        def dfs(i, target, total):
            if target==total:
                res.append(sublist.copy())
                return
            
            if target<total or i>=len(nums):
                return
            sublist.append(nums[i])
            dfs(i, target, total+nums[i])
            sublist.pop()
            dfs(i+1, target, total)
        dfs(0,target,0)
        return res