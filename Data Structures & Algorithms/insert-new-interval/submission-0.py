class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = [newInterval]

        for start,end in intervals:
            start_i, end_i = stack.pop()

            if start <= start_i <= end or start_i <= start <= end_i:
                newStart = start if start < start_i else start_i
                newEnd = end if end > end_i else end_i

                stack.append([newStart,newEnd])
            
            else:
                if start < start_i:
                    stack.append([start, end])
                    stack.append([start_i, end_i])
                else:
                    stack.append([start_i, end_i])
                    stack.append([start, end])
        
        return stack



"""
[[1,3]   [4,6]]    [2,5]

- edge cases of beginning and end

1. create stack output with newInterval first append
2. iterate across every current interval

3. check if top of stack overlaps with current interval
3a. if overlap, merge into new interval
3b. if no overlap, pop stack, append earlier start then later start

4. return stack


[1,6]
"""