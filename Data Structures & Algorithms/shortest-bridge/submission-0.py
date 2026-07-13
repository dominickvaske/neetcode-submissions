class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        first_island_shape = set()

        def dfs(r, c):
            first_island_shape.add((r,c))
            for dx, dy in DIRECTIONS:
                i = r + dx
                j = c + dy
                if (0 <= i < ROWS and
                    0 <= j < COLS and
                    grid[i][j] == 1 and
                    (i,j) not in first_island_shape):
                        first_island_shape.add((i,j))
                        dfs(i,j)

        def findFirstIsland(grid):
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        dfs(r,c) # map the whole first island
                        return

        def bfs(queue):
            distance = 0
            while queue:
                qLength = len(queue)

                for _ in range(qLength):
                    r, c = queue.popleft()
                    
                    for dx, dy in DIRECTIONS:
                        i = r + dx
                        j = c + dy

                        if (0 <= i < ROWS and
                            0 <= j < COLS and 
                            (i,j) not in first_island_shape):
                            if grid[i][j] == 1:
                                return distance
                            else:
                                first_island_shape.add((i,j))
                                queue.append((i,j))
                distance += 1

        findFirstIsland(grid)
        queue = deque(first_island_shape)
        return bfs(queue)
