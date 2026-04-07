class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val=self.stack[-1]
        self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        val = self.stack[-1]
        return val
        

    def getMin(self) -> int:
        if len(self.min_stack)>0:
            val= self.min_stack[-1]
            return val
        else:
            return None
        
