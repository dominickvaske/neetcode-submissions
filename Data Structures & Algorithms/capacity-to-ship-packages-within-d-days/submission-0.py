class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # must have at least max weight capacity to take that weight
        # by itself on one day
        l, r = max(weights), sum(weights)
        minCap = r
        
        def checker(test_capacity):
            timeToShip = 1
            currSum = 0
            for weight in weights:
                if currSum + weight > test_capacity:
                    currSum = weight
                    timeToShip += 1
                else:
                    currSum += weight
            return timeToShip
        
        while l <= r:
            capacity = (l+r) // 2

            timeToShip = checker(capacity)

            if timeToShip <= days:
                minCap = capacity
                r = capacity - 1
            else:
                l = capacity + 1
        
        return minCap
