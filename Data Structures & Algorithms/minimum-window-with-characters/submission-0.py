class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)==0:
            return ""
        countT, window = {}, {}

        for c in t:
            if c in countT:
                countT[c]+=1
            else:
                countT[c]=1
        res, reslen = [-1,-1], float('inf')
        l=0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c= s[r]
            window[c]=1 + window.get(c,0)

            if c in countT and countT[c]==window[c]:
                have+=1

            while have==need:
                if r-l+1 < reslen:
                    reslen=r-l+1
                    res=[l,r]

                #pop from left
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen != float("infinity") else ""

