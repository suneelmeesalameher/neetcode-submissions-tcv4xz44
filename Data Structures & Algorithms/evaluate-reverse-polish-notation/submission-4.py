class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=["+","-","*","/"]
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                num1=int(stack.pop())
                num2=int(stack.pop())
                if token=="+":
                    stack.append(num2+num1)
                elif token=="-":
                    stack.append(num2-num1)
                elif token=="*":
                    stack.append(num2*num1)
                elif token=="/":
                    stack.append(num2/num1)
        return int(stack[0])
