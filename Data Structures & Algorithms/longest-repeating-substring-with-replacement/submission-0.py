class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxlength=0
        freqcount={}
        maxfreqinmap=0
        for r in range(0,len(s)):
            if s[r] in freqcount:
                freqcount[s[r]]+=1
            else:
                freqcount[s[r]]=1
            maxfreqinmap=max(maxfreqinmap, freqcount[s[r]])
            #if r-l+1 - maxfreqinmap==k:
                #maxlength=max(maxlength, r-l+1)
            if r-l+1 - maxfreqinmap>k:
                #reduce the window  size
                freqcount[s[l]]-=1
                l+=1
            maxlength=max(maxlength, r-l+1)
        return maxlength