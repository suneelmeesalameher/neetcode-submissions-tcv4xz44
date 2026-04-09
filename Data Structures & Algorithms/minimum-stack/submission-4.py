class MinStack:

    def __init__(self):
        self.stack= []
        


    def push(self, val: int) -> None:
        self.stack.append(val)
    

    def pop(self) -> None:
        self.stack.pop()


        

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) else None

        

    def getMin(self) -> int:
        mini=float('inf')
        for num in self.stack:
            mini=min(mini, num)
        return mini

        
