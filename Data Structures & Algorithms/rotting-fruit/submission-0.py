class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0 
        while queue: 
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            if queue: 
                time += 1

        return time if fresh == 0 else -1