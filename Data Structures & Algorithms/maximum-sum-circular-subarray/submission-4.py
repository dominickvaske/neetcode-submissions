class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sub = nums[0]
        max_so_far = 0
        for num in nums:
            max_so_far += num
            max_so_far = max(max_so_far, num)
            max_sub = max(max_sub, max_so_far)

        min_sub = nums[0]
        min_so_far = 0
        for num in nums:
            min_so_far += num
            min_so_far = min(min_so_far, num)
            min_sub = min(min_so_far, min_sub)

        total_sum = sum(nums)

        if max_sub < 0:
            return max_sub
        
        return max(max_sub, total_sum - min_sub)
