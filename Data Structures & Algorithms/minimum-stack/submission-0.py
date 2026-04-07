class MinStack:

    def __init__(self):
        self.stk=[]

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        minv=self.stk[0]
        for i in range(1,len(self.stk)):
            if minv>self.stk[i]:
                minv=self.stk[i]
        return minv
        
