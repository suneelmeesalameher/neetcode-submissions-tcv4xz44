class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        revs=s[::-1]
        if s== revs:
            return True
        else:
            return False
        