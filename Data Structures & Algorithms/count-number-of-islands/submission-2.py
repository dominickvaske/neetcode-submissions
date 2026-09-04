class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # implement bfs
        def bfs(i,j):
            queue = deque([(i,j)])

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx,ny))             

        # iterate over all spaces and look for island starts
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i,j)
                    grid[i][j] = "0"
                    num_islands += 1
        
        return num_islands