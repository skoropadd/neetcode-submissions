class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        target_color = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != target_color:
                return None
            elif image[r][c] == target_color:
                image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return image

        dfs(sr, sc)
        return image