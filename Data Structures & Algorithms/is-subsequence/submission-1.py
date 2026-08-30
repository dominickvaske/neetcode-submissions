class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        curr = 0
        for char in t:
            if curr == len(s)-1:
                return True
            if char == s[curr]:
                curr += 1
        
        return False