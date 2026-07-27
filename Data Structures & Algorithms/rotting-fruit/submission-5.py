class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        rottens = []
        fresh_count = 0
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rottens.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0

        def bfs(start):
            queue = deque(start)
            time = -1
            remaining_fresh = fresh_count
            while queue:
                qLen = len(queue)
                
                for _ in range(qLen):
                    i, j = queue.popleft()

                    for dx, dy in DIRECTIONS:
                        new_i, new_j = i+dx, j+dy

                        if (0 <= new_i < ROWS and
                            0 <= new_j < COLS and
                            grid[new_i][new_j] == 1):
                            grid[new_i][new_j] = 2
                            remaining_fresh -= 1
                            queue.append((new_i,new_j))

                time += 1   
            return time if remaining_fresh == 0 else -1

        return bfs(rottens)