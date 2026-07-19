class Solution:
    def jump(self, nums: List[int]) -> int: 
        curr = 0
        ans = 0
        while curr < len(nums)-1:
            jumpMax = nums[curr]
            possJump, nextIndex = 0, 0
            step = 1

            if curr + jumpMax >= len(nums)-1:
                ans += 1
                return ans
            
            while step <= jumpMax and curr + step < len(nums):
                if curr+step+ nums[curr + step] >= possJump:
                    possJump = nums[curr + step]+curr+step
                    nextIndex = curr + step
                step += 1
            
            curr = nextIndex
            ans += 1

        return ans

# curr: 2
# jM: 2
# pJ: 0
# nI: 0
# step: 1
# ans = 1