class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping ={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:
            if bracket in mapping:
                if not stack or stack[-1]!=mapping[bracket]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)
        if len(stack)==0:
            return True
        else:
            return False