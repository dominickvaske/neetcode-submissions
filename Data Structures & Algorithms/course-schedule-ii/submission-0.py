class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list and indegree count for courses
        neighbors = defaultdict(list)
        indegree = defaultdict(int)
        for crs, pre in prerequisites:
            neighbors[pre].append(crs)
            indegree[crs] += 1
        
        # build initial queue with all courses with
        # no prereqs (ie indegree = 0)
        queue = deque([crs for crs in range(numCourses)
                        if indegree[crs] == 0])
        topo_order = []

        # now run bfs from all starting courses
        while queue:
            crs = queue.popleft()
            # crs in queue are free to take
            topo_order.append(crs)

            for neighbor in neighbors[crs]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) != numCourses:
            return []
        
        return topo_order


        
