class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dirs1={}
        dirs2={}
        if len(s1)>len(s2):
            return False
        
        for s in s1:
            if s in dirs1:
                dirs1[s]+=1
            else:
                dirs1[s]=1
        
        l=0
        for r in range(len(s2)):

            if s2[r] in dirs2:
                dirs2[s2[r]]+=1
            else:
                dirs2[s2[r]]=1

            if r-l+1==len(s1):
                # position l to l+=1
                if dirs1==dirs2:
                    return True

                if dirs2[s2[l]]>1:
                    dirs2[s2[l]]-=1
                    
                else:
                    del dirs2[s2[l]]
                l+=1
                
        
        return False
                
                
                

