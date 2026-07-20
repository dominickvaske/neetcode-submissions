class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        DP = [0]*(n+2)

        for i in range(n-1, -1, -1):
            DP[i] = cost[i] + min(DP[i+1], DP[i+2])

        return min(DP[0], DP[1])

"""
S: Let DP[i] define the minimum cost to reach top of stairs from ith position
R: DP[i] = cost[i] + min(DP[i+1],DP[i+2])
T: i goes from n to 0
B: DP[n] = 0 (no cost to reach end from the end)
O: return min(DP[0],DP[1])

"""