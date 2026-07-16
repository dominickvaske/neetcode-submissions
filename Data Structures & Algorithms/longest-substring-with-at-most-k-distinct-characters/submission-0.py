class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seenCharacters = defaultdict(int)
        left = ans = 0

        for right in range(len(s)):
            seenCharacters[s[right]] += 1

            while len(seenCharacters) > k:
                seenCharacters[s[left]] -= 1
                if seenCharacters[s[left]] == 0:
                    del seenCharacters[s[left]]
                
                left += 1
            
            ans = max(ans, right-left+1)

        return ans
