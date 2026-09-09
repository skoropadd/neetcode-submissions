class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pcf = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or heights[r][c] < prev_height):
                return 
            
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for r in range(rows):
            c = 0
            dfs(r, c, pcf, heights[r][c])
        
        for c in range(cols):
            r = 0
            dfs(r, c, pcf, heights[r][c])

        for r in range(rows):
            c = cols - 1
            dfs(r, c, atl, heights[r][c])
        
        for c in range(cols):
            r = rows - 1
            dfs(r, c, atl, heights[r][c])

        return [[r, c] for r, c in pcf & atl]