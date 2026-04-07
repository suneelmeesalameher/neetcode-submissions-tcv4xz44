class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        r=0
        maxlength=0

        for r in range(0, len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
                
            charset.add(s[r])
            maxlength=max(maxlength, r-l+1)
        return maxlength