class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydir1 = {}
        mydir2 = {}
        for c in s:
            if c in mydir1:
                mydir1[c] =mydir1[c]+1
            else:
                mydir1[c]=1
        for c in t:
            if c in mydir2:
                mydir2[c] =mydir2[c]+1
            else:
                mydir2[c]=1
        if mydir1==mydir2:
            return True
        else:
            return False