class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            prevVal, prevMin = self.stack[-1]
            if val < prevMin:
                self.stack.append((val,val))
            else:
                self.stack.append((val,prevMin))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            prevVal, _ = self.stack[-1]
            return prevVal

        return None

    def getMin(self) -> int:
        if self.stack:
            _, currMin = self.stack[-1]
            return currMin
        return None


