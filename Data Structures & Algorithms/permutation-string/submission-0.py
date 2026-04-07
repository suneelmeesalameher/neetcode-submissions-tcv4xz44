class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1={}
        freqs2={}
        l=0
        for x in s1:
            if x in freqs1:
                freqs1[x]+=1
            else:
                freqs1[x]=1
        for r in range(0, len(s2)):
            if s2[r] in freqs2:
                freqs2[s2[r]]+=1
            else:
                freqs2[s2[r]]=1

            if r-l+1 == len(s1):
                if freqs1==freqs2:
                    return True
                else:
                    #reduce window size
                    freqs2[s2[l]]-=1
                    if freqs2[s2[l]]==0:
                        del freqs2[s2[l]]
                    l+=1
        return False