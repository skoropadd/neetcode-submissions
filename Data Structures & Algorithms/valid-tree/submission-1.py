class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        
        graphMap = {i:[] for i in range(n)}
        for n1, n2 in edges: 
            graphMap[n1].append(n2)
            graphMap[n2].append(n1)

        visited = set()
        def dfs(node, parent): 
            visited.add(node)
            for neighbor in graphMap[node]:
                if neighbor == parent: continue 
                if neighbor in visited: return False 
                if not dfs(neighbor, node): return False
            return True 
            
        # Run DFS once from node 0. If it's valid AND reaches all n nodes, it's a tree.
        if not dfs(0, -1): return False
        return len(visited) == n 