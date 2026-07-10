class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        rottenFruit = []
        freshFruit = 0
        time = 0
        
        def bfs(q):
            nonlocal time, freshFruit
            queue = deque(q)

            while queue:
                qLength = len(queue)

                for _ in range(qLength):
                    i,j = queue.popleft()
                    for dx, dy in DIRECTIONS:
                        if ((0 <= i+dx < ROWS) and
                            (0 <= j+dy < COLS) and
                            grid[i+dx][j+dy] == 1):
                            # print(f"new rotten:", i+dx,j+dy)
                            grid[i+dx][j+dy] = 2
                            freshFruit -= 1
                            queue.append((i+dx,j+dy))

                if len(queue) > 0:
                    time += 1
                # print(f"fresh fruit:", freshFruit)
                if freshFruit == 0:
                    return time    
            return -1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rottenFruit.append((i,j))
                elif grid[i][j] == 1:
                    freshFruit += 1
        
        if freshFruit == 0:
            return 0
        return bfs(rottenFruit)