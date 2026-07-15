class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        indegree = defaultdict(int)
        ans = []

        for crs, pre in prerequisites:
            neighbors[pre].append(crs)
            indegree[crs] += 1
        

        def bfs(start_nodes):
            queue = deque(start_nodes)

            while queue:
                crs = queue.popleft()
                ans.append(crs)

                for nei in neighbors[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        starts = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                starts.append(crs)
        
        bfs(starts)
        
        return len(ans) == numCourses