class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        anagramset={}
        for x in strs:
            check= tuple(sorted(x))
            if(check not in anagramset):
                anagramset[check]=[]
            anagramset[check].append(x)
        group=list(anagramset.values())
        return group
