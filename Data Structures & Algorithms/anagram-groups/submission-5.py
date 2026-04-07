class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydir=defaultdict(list)
        ans=[]

        for s in strs:
            key=''.join(sorted(s))
            #if mydir[key]:
            mydir[key].append(s)
            #else:
            #    mydir[key]=[s]
        
        for key, value in mydir.items():
            ans.append(value)
        
        return ans