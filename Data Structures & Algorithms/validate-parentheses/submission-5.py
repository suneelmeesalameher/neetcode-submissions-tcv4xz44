class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for par in s:
            if par == '{' or par=='(' or par == '[':
                stk.append(par)
            else:
                if par=='}':
                    if stk[-1]=='{':
                        stk.pop()
                    else:
                        return False
                if par==']':
                    if stk[-1] and stk[-1]=='[':
                        stk.pop()
                    else:
                        return False
                if par==')':
                    if stk[-1]=='(':
                        stk.pop()
                    else:
                        return False
        
        return True if len(stk)==0 else False
        

        