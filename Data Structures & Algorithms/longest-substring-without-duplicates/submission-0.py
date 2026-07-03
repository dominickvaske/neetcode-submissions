class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counts = defaultdict(int)
        left = 0
        right = 0
        ans = 0

        while right < len(s):
            counts[s[right]] += 1

            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans

"""
abcabcbb


"""



