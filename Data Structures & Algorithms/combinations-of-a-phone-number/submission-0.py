class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []

        phonemap={
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }

        res=[]
        sublist=""
        
        
        def dfs(i, sublist):
            if len(sublist)==len(digits):
                res.append(sublist)
                return

            if digits[i] in phonemap:
                for j in phonemap[digits[i]]:
                    dfs(i+1, sublist+j)


       
        dfs(0, sublist)

        return res
        
            
            


            
            

