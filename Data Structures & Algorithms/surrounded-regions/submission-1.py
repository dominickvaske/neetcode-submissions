class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # find all those on the edge
        edges = []
        for i in range(ROWS):
            for j in range(COLS):
                if ((i == 0 or i == ROWS - 1 or
                    j == 0 or j == COLS - 1) and
                    board[i][j] == 'O'):
                        edges.append((i,j))
                        board[i][j] = 'T'
        
        def bfs(edges):
            queue = deque(edges)

            while queue:
                i, j = queue.popleft()
                
                for dx, dy in directions:
                    new_i = i + dx
                    new_j = j + dy

                    if (0 <= new_i < ROWS and
                        0 <= new_j < COLS and
                        board[new_i][new_j] == 'O'):
                        board[new_i][new_j] = 'T'
                        queue.append((new_i,new_j))

        
        bfs(edges)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'