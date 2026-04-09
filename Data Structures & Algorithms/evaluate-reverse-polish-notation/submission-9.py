class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation={
            "+":"+",
            "-":"-",
            "*":"*",
            "/":"/"
        }

        stack=[]
        for t in tokens:
            if t not in operation:
                stack.append(int(t))
            else:
                val1, val2=stack.pop(), stack.pop()
                if operation[t]=="+":
                    newval=val1+val2
                elif operation[t]=="-":
                    newval=val1-val2
                elif operation[t]=="*":
                    newval=val1*val2
                elif operation[t]=="/":
                    newval=val1//val2
                stack.append(newval)
        return int(stack[-1])
