class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mydict={}
        maxval=0
        ans=None
        for num in nums:
            if num in mydict:
                mydict[num]+=1
            else:
                mydict[num]=1
        print(mydict)
        for key, val in mydict.items():
            if maxval<val:
                ans=key
                maxval=val
        return ans