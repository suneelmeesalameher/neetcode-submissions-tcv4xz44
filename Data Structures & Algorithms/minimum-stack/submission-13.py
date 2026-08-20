class MinStack:

    def __init__(self):
        self.stk=[]
        self.minstk=[]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minstk)==0 or self.minstk[-1]>= val:
            self.minstk.append(val)
        

    def pop(self) -> None:
        val = self.stk.pop()
        if val == self.minstk[-1]:
            self.minstk.pop()
        
        

    def top(self) -> int:
        return self.stk[-1]
    
        

    def getMin(self) -> int:
        return self.minstk[-1]
       
        
