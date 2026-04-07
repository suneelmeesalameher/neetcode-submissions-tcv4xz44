class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dir1={}
        dir2={}
        if(len(s)!=len(t)):
            return False
        for x in s:
            if x in dir1:
                dir1[x]=dir1[x]+1
            else:
                dir1[x]=1
        for x in t:
            if x in dir2:
                dir2[x]=dir2[x]+1
            else:
                dir2[x]=1
        if(dir1==dir2):
            return True
        else:
            return False