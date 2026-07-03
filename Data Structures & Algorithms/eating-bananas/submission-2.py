class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # fastest needed rate is largest pile
        hi = res = max(piles)
        lo = 1

        # need to check if current rate will get through all piles
        # in time
        def check(piles, mid, h):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            
            return totalTime <= h

        # binary search to find best rate
        while lo <= hi:
            mid = (lo + hi) // 2

            if check(piles, mid, h) == True:
                # check for a lower speed
                hi = mid - 1
                res = mid
            else:
                #find a higher speed
                lo = mid + 1
        
        return res