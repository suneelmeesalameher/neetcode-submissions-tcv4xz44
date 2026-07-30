class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydir={}
        res=[]
        #sort the words
        for word in strs:
            key= "".join(sorted(word))
            if key in mydir:
                mydir[key].append(word)
            else:
                mydir[key]= [word]
        
        for key, value in mydir.items():
            res.append(value)
        return sorted(res)


        # Raw DOG method
        # directoryofdir={}
        # overallDirect=[]

        # for word in strs:
        #     mydir={}
        #     for w in word:
        #         mydir[w]= mydir.get(w,0)+1
        #     if tuple(sorted(mydir.items())) in directoryofdir:
        #         directoryofdir[tuple(sorted(mydir.items()))].append(word)
        #     else:
        #         directoryofdir[tuple(sorted(mydir.items()))]=[word]
        
        # for key, value in directoryofdir.items():
        #     overallDirect.append(value)
    
        # return sorted(overallDirect)

