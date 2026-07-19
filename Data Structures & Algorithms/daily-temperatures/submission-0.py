class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, prev_temp = stack.pop()
                output[j] = i - j
            
            stack.append((i,temp))

        return output