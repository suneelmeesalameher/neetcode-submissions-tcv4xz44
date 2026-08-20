class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr={
            '+': True, 
            '-': True,
            '*': True, 
            '/': True
            } 
        stk=[]

        for vals in tokens:
            if vals in opr:
                secval=stk.pop()
                fival = stk.pop()
                if vals=='+':
                    thival = fival+secval
                    stk.append(thival)
                
                elif vals=='-':
                    thival = fival-secval
                    stk.append(thival)
                
                elif vals=='*':
                    thival = fival*secval
                    stk.append(thival)
                
                elif vals=='/':
                    thival = fival/secval
                    stk.append(thival)
                
            else:
                stk.append(int(vals))
        return stk[-1]

