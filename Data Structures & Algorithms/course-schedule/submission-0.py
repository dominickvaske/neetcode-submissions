class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # create a visited set
        visited = set()

        def dfs(crs):
            # check if course already been seen
            if crs in visited:
                return False
            # check if crs has no prereqs
            elif preMap[crs] == []:
                return True
            
            # must cycle through all prereqs of crs
            # to see if they can be taken
            visited.add(crs)
            for pre in preMap[crs]:
                # check if pre req can't be taken
                if not dfs(pre):
                    return False
            visited.remove(crs)
            # since crs is fine, remove prereq list
            preMap[crs] = []
            return True

        # run through all courses and check if
        # they can be taken without issue
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

