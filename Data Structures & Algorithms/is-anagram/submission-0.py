class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = defaultdict(int)

        for letter in s:
            letterCount[letter] += 1
        
        for letter in t:
            if letter not in letterCount:
                return False
            elif letterCount[letter] - 1 < 0:
                return False
            letterCount[letter] -= 1
        
        for letter in letterCount:
            if letterCount[letter] > 0:
                return False

        return True
