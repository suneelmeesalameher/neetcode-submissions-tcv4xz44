class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength=''
        if len(s)==1:
            return s[0]
        for i in range(0, len(s)):
            j=1
            while i-j>-1 and i+j<len(s):
                if s[i-j]==s[i+j]:
                    subset=s[i-j:i+j+1]
                    if len(maxlength)<len(subset):
                        maxlength=subset
                    j+=1
                else :
                    break
        
        for i in range(0, len(s)):
            j=1
            while i-j>-1 and i+j-1<len(s):
                if s[i-j]==s[i+j-1]:
                    subset=s[i-j:i+j]
                    if len(maxlength)<len(subset):
                        maxlength=subset
                    j+=1
                else :
                    break
        if len(maxlength)==0:
            return s[0]
        return maxlength
                

                
