class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydir={}
        mydir2={}

        for s in s1:
            if s in mydir:
                mydir[s]+=1
            else:
                mydir[s]=1
        
        left=0
        for right in range(len(s2)):
            if s2[right] in mydir2:
                mydir2[s2[right]]+=1
            else:
                mydir2[s2[right]]=1
            if right-left+1==len(s1):
                if mydir==mydir2:
                    return True
                else:
                    ##moving left pointer
                    mydir2[s2[left]]-=1
                    if mydir2[s2[left]]==0:
                        del mydir2[s2[left]]
                    left+=1
        return False

