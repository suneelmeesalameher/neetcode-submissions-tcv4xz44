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
                val2, val1=int(stack.pop()), int(stack.pop())
                if t =="+":
                    newval=val1+val2
                elif t =="-":
                    newval=val1-val2
                elif t =="*":
                    newval=val1*val2
                elif t =="/":
                    newval=val1/val2
                stack.append(newval)
        return int(stack[-1])
