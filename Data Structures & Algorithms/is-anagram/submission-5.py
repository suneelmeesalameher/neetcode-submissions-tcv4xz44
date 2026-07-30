class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydir1={}
        mydir2={}
        for s in s:
            #if s in mydir1:
            #    mydir1[s]=+1
            #else:
            #    mydir1[s]=1
            mydir1[s]=(mydir1.get(s, 0)) + 1
        
        for t in t:
            #if t in mydir2:
            #    mydir2[t]=+1
            #else:
            #    mydir2[t]=1

            mydir2[t]=mydir2.get(t,0) + 1
        
        return True if mydir1 == mydir2 else False