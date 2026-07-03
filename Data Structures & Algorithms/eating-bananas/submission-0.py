class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles) #upper bound for k since will only take 1 hour for every pile
        candidate = float('inf')

        def eatFunction(k, piles_copy):
            hours = 0
            for pile in piles_copy:
                hours += math.ceil(pile / k)
            
            return hours

        while start <= end:
            piles_copy = piles.copy()
            mid = (start + end) // 2

            timeToEat = eatFunction(mid, piles_copy)

            if timeToEat > h:
                start = mid + 1
            else:
                candidate = min(candidate, mid)
                end = mid - 1
        
        return candidate
