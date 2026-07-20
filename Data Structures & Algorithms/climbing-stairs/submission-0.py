class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0]*(n+2)
        DP[n] = 1

        for i in range(n-1,-1,-1):
            DP[i] = DP[i+1] + DP[i+2]

        return DP[0]
"""
S: Let DP[i] be the number of distinct ways to climb a staircase
    from the ith stair to the top (n)
R: DP[i] = DP[i+1] + DP[i+2]
T: i goes from n->1
B: DP[n] = 1 ; 1 successful way to reach the top
O: desire DP[0]

"""