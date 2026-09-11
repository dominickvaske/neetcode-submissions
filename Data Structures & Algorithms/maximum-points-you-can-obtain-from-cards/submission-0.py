class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = right = 0
        minSum = 0
        cardPointSum = sum(cardPoints)

        while right < n-k:
            minSum += cardPoints[right]
            right += 1

        tmp = minSum
        while right < n:
            tmp += cardPoints[right]
            tmp -= cardPoints[left]
            left += 1
            right += 1

            minSum = min(minSum, tmp)
        
        return cardPointSum - minSum

