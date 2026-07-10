class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            queue = deque([(i,j)])

            while queue:
                qlength = len(queue)

                for _ in range(qlength):
                    curr_i, curr_j = queue.popleft()

                    for dx, dy in directions:
                        neighbor_i, neighbor_j = curr_i+dx, curr_j+dy
                        if ((0 <= neighbor_i < ROWS) and
                            (0 <= neighbor_j < COLS) and
                            grid[neighbor_i][neighbor_j] != 0 and
                            grid[neighbor_i][neighbor_j] != -1):

                            if (grid[neighbor_i][neighbor_j] == INF or
                               1+grid[curr_i][curr_j] < grid[neighbor_i][neighbor_j]):
                                grid[neighbor_i][neighbor_j] = grid[curr_i][curr_j] + 1
                                queue.append((neighbor_i, neighbor_j))


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i,j)