class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        left = 0
        currSum = 0
        # get initial window to find max possible unsatisfied
        for i in range(minutes):
            currSum += customers[i] if grumpy[i] == 1 else 0
        
        # use sliding window to find max window of unhappy customers and associated indices
        greatest = currSum
        start, end = 0, minutes-1 #interval of best range (non-inclusive minutes)
        for right in range(minutes, len(customers)):
            if grumpy[right]:
                currSum += customers[right]
            if grumpy[left]:
                currSum -= customers[left]
            left += 1

            if currSum > greatest:
                start, end = left, right
                greatest = currSum
        
        ans = 0
        for j in range(len(customers)):
            if start <= j <= end:
                ans += customers[j]
            else:
                ans += customers[j] if not grumpy[j] else 0
        
        print(start, end)
        return ans
        




