class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redCount = 0
        whiteCount = 0
        blueCount = 0

        for color in nums:
            if color == 0:
                redCount += 1
            elif color == 1:
                whiteCount += 1
            else:
                blueCount += 1
        

        for i in range(redCount):
            nums[i] = 0
        
        for j in range(whiteCount):
            nums[j+redCount] = 1
        
        for k in range(blueCount):
            nums[k+redCount+whiteCount] = 2