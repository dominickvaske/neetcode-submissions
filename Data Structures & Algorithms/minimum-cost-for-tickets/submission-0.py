import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        DP = [0]*(n+1)

        for i in range(n-1,-1,-1):
            # Option 1: buy day pass
            cost1 = DP[i+1] + costs[0]

            # Option 2: buy 7 day pass
            # first, find next day >= days[i] + 7
            idx7 = bisect.bisect_left(days, days[i]+7, i, n)
            cost2 = DP[idx7] + costs[1]

            # Option 3: buy 30 day pass
            idx30 = bisect.bisect_left(days, days[i]+30, i, n)
            cost3 = DP[idx30] + costs[2]

            DP[i] = min(cost1, cost2, cost3)
        
        return DP[0]
            



"""
S: Let DP be an array where DP[i] represents the optimal price from day i onward
O: We want DP[0]
R: DP[i]:=
    if days[i]  DP[i+1] + cost[0] (single day) 
    if days[i]
T: i: n-2 -> 0
B: DP[n-1] = costs[0]


"""