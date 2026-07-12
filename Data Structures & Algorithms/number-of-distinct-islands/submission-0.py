class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1,0),(-1,0),(0,1), (0,-1)]
        distinct_shapes = set()

        def bfs(start_i,start_j):
            queue = deque([(start_i,start_j)])
            grid[start_i][start_j] = 0
            shape = []

            while queue:
                i, j = queue.popleft()
                shape.append((i-start_i, j-start_j))

                for dx, dy in DIRECTIONS:
                    new_i = i+dx
                    new_j = j+dy

                    if (0 <= new_i < ROWS and
                        0 <= new_j < COLS and
                        grid[new_i][new_j] == 1):

                        queue.append((new_i, new_j))
                        grid[new_i][new_j] = 0
                    
            return tuple(shape)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    island_shape = bfs(i, j)
                    distinct_shapes.add(island_shape)

        return len(distinct_shapes)