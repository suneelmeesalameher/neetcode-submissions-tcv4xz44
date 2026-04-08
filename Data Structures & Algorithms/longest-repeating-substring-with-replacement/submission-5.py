class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        maxfreq=0
        freq={}
        l,r=0,0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            maxfreq=max(maxfreq, freq[s[r]])
            if r-l+1 - maxfreq>k:
                freq[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            
        return maxlen



        # while r<len(s):
        #     if k>0:
        #         if s[r] not in chars:
        #             if len(chars)>0:
        #                 k-=1
        #             chars[s[r]]=1
        #         else:
        #             chars[s[r]]+=1
        #         maxlen=max(maxlen, r-l+1)
        #         r+=1
        #     else:
        #         ##time to remove
        #         maxlen=max(maxlen, r-l+1)
        #         while k==0:
        #             if chars[s[l]]==1:
        #                 del chars[s[l]]
        #             else:
        #                 chars[s[l]]-=1
        #             l+=1
        #             k+=1
        # return maxlen

                



