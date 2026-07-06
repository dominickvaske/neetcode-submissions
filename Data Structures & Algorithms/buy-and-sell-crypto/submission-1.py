class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ans = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r]-prices[l])
            else:
                l = r
            r += 1
        
        return ans
        