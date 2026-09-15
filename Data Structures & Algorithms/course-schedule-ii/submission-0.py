class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        complited = set()
        res = []

        def dfs(crs):
            if crs in visited: return False 
            if crs in complited: return True 

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            complited.add(crs)
            visited.remove(crs)
            res.append(crs)

            return True 

        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return res 
