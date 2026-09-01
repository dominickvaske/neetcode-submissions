class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_key = max(counts, key=counts.get)
        return max_key