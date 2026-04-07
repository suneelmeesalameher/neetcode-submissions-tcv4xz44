class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(0, len(s)):
            j=1
            while i-j>-1 and i+j<len(s):
                if s[i-j]==s[i+j]:
                    res+=1
                    j+=1
                else:
                    break
        for i in range(0, len(s)):
            j=1
            while i-j>-1 and i+j-1<len(s):
                if s[i-j] == s[i+j-1]:
                    res+=1
                    j+=1
                else:
                    break
        return res + len(s)