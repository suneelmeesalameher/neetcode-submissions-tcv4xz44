class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        pre=[nums[0]]
        for i in range(1,len(nums)):
            mul= nums[i]*pre[i-1]
            pre.append(mul)
        check=list(reversed(nums))
        post=[check[0]]
        for i in range(1,len(check)):
            mul= check[i]*post[i-1]
            post.append(mul)
        post=list(reversed(post))
        pre.insert(0, 1)
        post.append(1)
        for i in range(0,len(nums)):
            x=pre[i]
            y=post[i+1]
            ans.append(x*y)
        return ans
            
            
