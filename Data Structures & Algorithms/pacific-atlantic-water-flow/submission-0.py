class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or heights[r][c] > prev_height):
                return 
            if r == 0 or c == 0:
                self.pcf = True 
            if r == rows - 1 or c == cols - 1:
                self.atl = True 
            
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for r in range(rows):
            for c in range(cols):
                visited = set()
                self.pcf = False
                self.atl = False
                dfs(r, c, visited, heights[r][c])
                if self.pcf and self.atl:
                    res.append((r, c))

        return res 