class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            tmp = nums[mid]

            if tmp == target:
                return mid
            elif tmp > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
