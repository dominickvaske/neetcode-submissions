class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operators:
                secondOperator = stack.pop()
                firstOperator = stack.pop()

                if token == '+':
                    stack.append(firstOperator+secondOperator)
                elif token == "-":
                    stack.append(firstOperator-secondOperator)
                elif token == "*":
                    stack.append(firstOperator*secondOperator)
                else:
                    stack.append(int(firstOperator / secondOperator))
            else:
                stack.append(int(token))
            # print(stack)
        
        return stack.pop()


