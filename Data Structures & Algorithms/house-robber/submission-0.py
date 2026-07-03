class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        DP = [0] * n

        if n < 2:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        else:
            DP[-1] = nums[-1]
            DP[-2] = max(DP[-1], nums[-2])

            for i in range(n-3, -1, -1):
                DP[i] = max(DP[i+2] + nums[i], DP[i+1])
            
            return DP[0]

# S: Define DP[i] = max mount of money you can rob from house i onward
# O: Return DP[0] (max amount of money that can be robbed considering all houses)
# R: DP[i] = max(DP[i+2] + nums[i], DP[i+1])
# T: start from i = n-3 down to 1
# B: DP[n-1] = nums[n-1], DP[n-2] = max(DP[n-1], nums[n-2])