class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 0
        while n > 0:
            if n >= step + 1:
                n -= (step + 1)
                step += 1
            else:
                return step
        
        return step
