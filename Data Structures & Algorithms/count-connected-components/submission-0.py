class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = 0 
        visited = set()
        
        nodeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        def dfs(node):
            if node in visited: return 

            visited.add(node)
            for neighbors in nodeMap[node]:
                dfs(neighbors)
        
        for node in nodeMap:
            if node not in visited: 
                res += 1
                dfs(node)
        
        return res 


