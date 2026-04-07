class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        group={}
        for i,num in enumerate(nums):
            target=-num
            leftptr=i+1
            rightptr=len(nums)-1
            while leftptr<rightptr:
                sumcheck=nums[leftptr]+nums[rightptr]
                if sumcheck == target:
                    ans.append([num, nums[leftptr], nums[rightptr]])
                if sumcheck> target:
                    rightptr=rightptr-1
                else:
                    leftptr=leftptr+1
        unique=[]
        for x in ans:
            if x not in unique:
                unique.append(x)
        return unique

