class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=[]
        anaSet={}
        for string in strs:
            sortedTup=tuple(sorted(string))
            if(sortedTup not in anaSet):
                anaSet[sortedTup]=[]
            anaSet[sortedTup].append(string)
        group=list(anaSet.values())
        return group