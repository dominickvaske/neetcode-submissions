class MinStack:

    def __init__(self):
        self.normalStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.normalStack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.normalStack.pop()

    def top(self) -> int:
        return self.normalStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
