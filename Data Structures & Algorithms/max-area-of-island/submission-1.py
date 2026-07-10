class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_islands = 0
        max_area = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            queue = deque([(i,j)])
            area = 1
            grid[i][j] = 0

            while queue:
                curr_length = len(queue)

                for _ in range(curr_length):
                    curr_i, curr_j = queue.popleft()

                    for dx, dy in directions:
                        if ((0 <= curr_i + dx < ROWS) and
                           (0 <= curr_j + dy < COLS) and
                           grid[curr_i+dx][curr_j+dy] == 1):

                            queue.append((curr_i+dx, curr_j+dy))
                            grid[curr_i+dx][curr_j+dy] = 0
                            area += 1
            return area


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    tmp_area = bfs(i, j)
                    max_area = max(max_area, tmp_area)


        return max_area
        