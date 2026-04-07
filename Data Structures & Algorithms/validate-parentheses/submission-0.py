class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in range(0,len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stk.append(s[i])
            else:
                if len(stk)==0:
                    return False
                    
                if s[i]==")":
                    if stk[-1]=="(":
                        stk.pop()
                    else:
                        return False
                if s[i]=="]":
                    if stk[-1]=="[":
                        stk.pop()
                    else:
                        return False
                if s[i]=="}":
                    if stk[-1]=="{":
                        stk.pop()
                    else:
                        return False
        if len(stk)==0:
            return True
        else:
            return False
                

        