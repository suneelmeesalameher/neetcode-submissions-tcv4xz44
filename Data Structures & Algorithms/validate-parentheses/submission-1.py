class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        last= None
        if len(s)==0:
            return True
        
        for bracket in s:
            if len(stack)>0:
                new = bracket
                if new == '}'  and stack[-1] =='{':
                    stack.pop()
                elif new == ']' and stack[-1]=='[':
                    stack.pop()
                elif new == ')' and stack[-1]=='(':
                    stack.pop()
                elif new =='{' or new=='(' or new =='[':
                    stack.append(new)
                else:
                    return False
            else:
                last=bracket
                if last == '}' or last==')' or last ==']':
                    return False
                else:
                    stack.append(last)
        if len(stack)==0: 
            return True 
        else:
            return False