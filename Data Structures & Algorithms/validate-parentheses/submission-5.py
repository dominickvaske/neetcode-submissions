class Solution:
    def isValid(self, s: str) -> bool:
        openType = ['[','{', '(']

        closedType = {']':'[', '}':'{', ')':'('}

        stack = []

        for bracket in s:
            if bracket in openType:
                stack.append(bracket)
            else:
                if not stack or closedType[bracket] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True