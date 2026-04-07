class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqcount={}
        left=0
        maxlen=0
        maxfrequency=0

        for right in range(len(s)):
            if s[right] in freqcount:
                freqcount[s[right]]+=1
            else:
                freqcount[s[right]]=1
            maxfrequency=max(maxfrequency, freqcount[s[right]])
            if right-left+1 - maxfrequency >k:
                freqcount[s[left]]-=1
                left+=1
            maxlen=max(maxlen, right-left+1)
        return maxlen

