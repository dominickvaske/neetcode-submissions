class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0]*(n+2)

        for i in range(n-1,-1,-1):
            DP[i] = max(0+DP[i+1],nums[i]+DP[i+2])
        
        return DP[0]


"""
S: Let DP[i] be the maximum amount you can steal from the ith house
R: DP[i] = nums[i] + max(DP[i+1], DP[i+2])
T: i: from n to 0
B: DP[n] = 0
O: return DP[0]
"""