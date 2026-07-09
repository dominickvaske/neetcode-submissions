class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # all remaining numbers positive
            if num > 0:
                break
            
            # skip duplicates:
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) -1 
            while l < r:
                num1 = nums[l]
                num2 = nums[r]

                total = num+num1+num2

                if total == 0:
                    res.append([num, num1, num2])
                    l += 1
                    r -= 1

                    # skip duplicate triplets
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res