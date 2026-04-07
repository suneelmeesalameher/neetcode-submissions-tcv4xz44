class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        count=0
        for x in nums:
            if x in freq:
                freq[x]=freq[x]+1
            else:
                freq[x]=1

        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_dict.items():
            ans.append(key[0])
            count=count+1
            if(count==k):
                break
        return ans

            


        