class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        # function to check if you can make at least p pairs
        # where difference is <= maxDifference
        def canMakePairs(maxDifference):
            pairs = 0
            i = 0
            # logic to check all pairs in nums to see if you can make p pairs
            while i < len(nums) - 1:
                diff = nums[i+1]-nums[i]

                if diff <= maxDifference:
                    pairs += 1
                    i += 2
                else:
                    i += 1

            return pairs >= p
        

        # conduct binary search on all possible differences
        right = nums[-1] - nums[0] # maximum possible difference in list
        left = 0
        ans = right
        while left <= right:
            mid = (left+right) // 2

            if canMakePairs(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans


