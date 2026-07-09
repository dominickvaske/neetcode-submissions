class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # print(f"Found position (0,4):", grid[0][4])
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for dx, dy in directions:
                    if (i+dx >= 0 and i+dx < len(grid)) and (j+dy >= 0 and j+dy < len(grid[0])):
                        dfs(i+dx, j+dy)
            else:
                return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if i == 0 and j == 4:
                #         print(f"Found position (0,4):", grid[i][j])
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands