class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val);
        if len(self.minStack)==0:
            self.minStack.append(val);
        elif self.minStack[-1]>=self.stack[-1]:
            self.minStack.append(val);
        

    def pop(self) -> None:
        val=self.stack.pop();
        if val==self.minStack[-1]:
            self.minStack.pop();
        

    def top(self) -> int:
        return self.stack[-1];

    def getMin(self) -> int:
        if len(self.minStack)>0:
            return self.minStack[-1];


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()