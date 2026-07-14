class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        left = 0
        ans = 0
        start = 0

        for start in range(k):
            currSum += arr[start]

        if currSum / k >= threshold:
            ans +=1

        for right in range(start+1, len(arr)):
            currSum += arr[right]
            currSum -= arr[left]
            left += 1

            if currSum / k >= threshold:
                ans += 1
        
        return ans