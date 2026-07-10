class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = defaultdict(int)
        ans = 0

        for right in range(len(s)):
            c = s[right]
            seen[c] += 1

            while seen[c] > 1:
                remove = s[left]
                seen[remove] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
