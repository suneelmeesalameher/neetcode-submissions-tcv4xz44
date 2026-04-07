class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxvalue=0
        mydir=defaultdict()
        ans=[]

        for num in nums:
            if num in mydir:
                mydir[num]+=1 
            else:
                mydir[num]=1
            maxvalue=max(maxvalue, mydir[num])
        
        counter=[[] for __ in range (maxvalue+1)]

        for key, value in mydir.items():

            counter[value].append(key)

        r=len(counter)-1
        while r>=0 and k>0:
            if len(counter[r])>0:
                #[2,3]
                li=counter[r]
                for v in counter[r]:
                    ans.append(v)
                    k-=1
            r-=1
        return ans

        
        



