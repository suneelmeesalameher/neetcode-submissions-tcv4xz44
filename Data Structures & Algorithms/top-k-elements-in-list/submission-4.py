class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #freq=[0]*len(nums)
        ans=[]
        mydir={}
        maxfreq=0
        for i in range(len(nums)):
            if nums[i] in mydir:
                mydir[nums[i]]+=1

            else:
                mydir[nums[i]]=1
            maxfreq=max(mydir[nums[i]],maxfreq)

        freq=[ [] for _ in range(maxfreq+1)]
        for key, value in mydir.items():
            freq[value].append(key)
            
        j=maxfreq
        while k!=0:
            for num in freq[j]:
                ans.append(num)
                k-=1
                if k==0:
                    break
            j-=1
            
        return ans



