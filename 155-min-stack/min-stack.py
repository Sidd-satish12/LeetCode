class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, val: int) -> None:
        if self.min_element is None:
            self.min_element = val
        if val < self.min_element:
            self.min_element = val
        self.stack.append((val,self.min_element))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_element = self.stack[-1][1]
        else:
            self.min_element = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()