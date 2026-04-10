class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring={}
        maxlength=0
        l=0
        r=0

        while r<len(s):
            if s[r] not in substring:
                substring[s[r]]=1
                r+=1
            else:
                if substring[s[l]]>1:
                    substring[s[l]]-=1
                else:
                    del substring[s[l]]
                l+=1
            maxlength=max(maxlength, r-l)
            
        return maxlength