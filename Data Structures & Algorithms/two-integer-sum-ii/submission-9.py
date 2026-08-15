class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftptr=0
        rightptr=len(numbers)-1
        ans=[]
        while leftptr<rightptr:
            sum_check=numbers[leftptr]+numbers[rightptr]
            if sum_check==target:
                ans.append(leftptr+1)
                ans.append(rightptr+1)
                return ans
            if sum_check>target:
                rightptr=rightptr-1
            else:
                leftptr=leftptr+1
            