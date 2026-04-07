class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mydir={}
        checker={}
        have=0 
        reslen=float('infinity')
        res=[-1,-1]
        for c in t:
            if c not in mydir:
                mydir[c]=1
            else:
                mydir[c]+=1
        need=len(mydir)
        l=0
        for right in range(len(s)):
            if s[right] in checker:
                checker[s[right]]+=1
            else:
                checker[s[right]]=1
            
            if s[right] in mydir and checker[s[right]]==mydir[s[right]]:
                have+=1

            while have==need:
                if (right-l+1)<reslen:
                    res=[l,right]
                    reslen=right-l+1
                
                checker[s[l]]-=1
                if s[l] in mydir and checker[s[l]]<mydir[s[l]]:
                    have-=1
                l+=1
        l,right=res
        return s[l:right+1] if reslen!=float('infinity') else ""