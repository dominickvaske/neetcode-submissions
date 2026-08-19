class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # if two prefix sums have the same remainder when divided by k, then
        # their difference is divisible by k

        prefixRemains = defaultdict(int)
        prefixRemains[0] = 1
        currSum = 0
        res = 0

        for num in nums:
            currSum += num
            remainder = currSum % k

            res += prefixRemains[remainder]
            prefixRemains[remainder] += 1
        
        return res
            