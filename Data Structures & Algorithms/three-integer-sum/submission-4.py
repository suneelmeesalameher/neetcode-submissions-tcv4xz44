class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res=[]
        for i in range(len(nums)):
            a=nums[i]
            if a>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            leftptr=i+1
            rightptr=len(nums)-1
            while leftptr<rightptr:
                total= nums[leftptr]+ nums[rightptr]+a
                if total==0:
                    res.append([a, nums[leftptr], nums[rightptr]])
                    leftptr+=1
                    rightptr-=1
                    while leftptr<rightptr and nums[leftptr]==nums[leftptr-1]:
                        leftptr+=1
                    while leftptr<rightptr and nums[rightptr]==nums[rightptr+1]:
                        rightptr-=1
                    
                if total>0:
                    rightptr-=1
                if total<0:
                    leftptr+=1
        
        
        return res      