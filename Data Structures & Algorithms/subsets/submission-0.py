class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for num in nums:
            newsubset=[curr + [num] for curr in result]
            result.extend(newsubset)
        return result     