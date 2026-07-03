class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areaMax = 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            elif grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            belowCount = dfs(grid, i+1, j)
            aboveCount = dfs(grid, i-1, j)
            rightCount = dfs(grid, i, j+1)
            leftCount = dfs(grid, i, j-1)

            return belowCount + aboveCount + rightCount + leftCount + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tempArea = dfs(grid, i, j)
                    areaMax = max(tempArea, areaMax)
        
        return areaMax