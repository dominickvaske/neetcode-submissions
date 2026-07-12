class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        currSum = 0
        res = 0
        prefixSums[0] += 1 # to cover the empty subarray / beginning
        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k
            
            res += prefixSums[diff]
            prefixSums[currSum] += 1
        
        return res
