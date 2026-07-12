class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        n = len(nums)
        for key in counts:
            if counts[key] > n // 3:
                res.append(key)
        
        return res