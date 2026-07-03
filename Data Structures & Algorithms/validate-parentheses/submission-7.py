class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myMap = {")":"(", "}":"{", "]":"["}
        openBrackets = ['(','{','[']
        for bracket in s:
            if bracket in openBrackets:
                myStack.append(bracket)
            else:
                if len(myStack) == 0:
                    return False
                elif myStack[-1] == myMap[bracket]:
                    myStack.pop()
                else:
                    return False
        
        if len(myStack) != 0:
            return False
        
        return True