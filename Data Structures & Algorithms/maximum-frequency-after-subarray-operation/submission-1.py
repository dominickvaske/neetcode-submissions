class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        base = 0
        for num in nums:
            if num == k:
                base += 1

        maxSum = 0

        for v in range(1,51):
            if v == k:
                continue
            
            currSum = 0

            for num in nums:
                if currSum < 0:
                    currSum = 0
                
                if num == v:
                    currSum += 1
                elif num == k:
                    currSum -= 1
            
                maxSum = max(maxSum, currSum)
        
        return base + maxSum