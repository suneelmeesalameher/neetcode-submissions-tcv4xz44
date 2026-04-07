class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stk=set()
        left=0
        maxLen=0
        for right in s:
            while right in stk:
                stk.remove(s[left])
                left+=1
            stk.add(right)
            maxLen=max(maxLen, len(stk))

            
        return maxLen

        