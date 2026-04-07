class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[[]]
        for nums in nums:
            leng=len(result)
            for i in range(0, leng):
                newsubset=result[i] + [nums]
                if newsubset not in result:
                    result.append(newsubset)
        return result      