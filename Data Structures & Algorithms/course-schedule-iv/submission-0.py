class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq_sets = defaultdict(set)
        
        # 1. Create adjacency list
        neighbors = defaultdict(list)
        indegree = defaultdict(int)
        for pre, crs in prerequisites:
            neighbors[pre].append(crs)
            indegree[crs] += 1
        
        start_nodes = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                start_nodes.append(crs)

        # 2. Use adjacency list to run top. sort
        topo_sort = []
        def bfs(start_nodes):
            queue = deque(start_nodes)

            while queue:
                crs = queue.popleft()
                topo_sort.append(crs)

                for neighbor in neighbors[crs]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                    
                    prereq_sets[neighbor].add(crs)
                    prereq_sets[neighbor].update(prereq_sets[crs])
        
        bfs(start_nodes)

        # iterate through queries and see if true
        ans = []

        for pre, crs in queries:
            if pre in prereq_sets[crs]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans