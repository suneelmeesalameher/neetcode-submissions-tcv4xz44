class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        opr=["+","-","*","/"]
        for x in tokens:
            if x not in opr:
                stk.append(x)
            else:
                num1=int(stk.pop())
                num2=int(stk.pop())
                if x=="+":
                    num3=num1+num2
                if x=="-":
                    num3=num2-num1
                if x=="*":
                    num3=num2*num1
                if x=="/":
                    num3=num2/num1
                stk.append(num3)
        return int(stk[0])  