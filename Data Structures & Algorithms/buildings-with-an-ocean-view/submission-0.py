class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        maxRight = 0
        output = []
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > maxRight:
                output.append(i)
                maxRight = heights[i]
        
        return output[::-1]