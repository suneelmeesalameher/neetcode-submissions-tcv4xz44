class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdir={}
        tdir={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sdir:
                sdir[s[i]]=1
            sdir[s[i]]=sdir[s[i]]+1
        
        for i in range(len(t)):
            if t[i] not in tdir:
                tdir[t[i]]=1
            tdir[t[i]]=tdir[t[i]]+1
        
        if sdir!=tdir:
            return False
            
        return True
        