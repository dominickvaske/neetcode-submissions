class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                ans = min(ans, right-left+1)
                currSum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans


# 2 1 5 1 5 3