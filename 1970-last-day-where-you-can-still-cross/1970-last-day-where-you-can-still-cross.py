
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def dfs(x, y, v):
            if x < 0 or x >= row or y < 0 or y >= col or v[x][y] or grid[x][y] == 0:
                return False
            if x == row - 1:
                return True
            v[x][y] = True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(x + dx, y + dy, v):
                    return True
            return False
        
        def check(m):
            for i in range(row):
                for j in range(col):
                    if grid[i][j] <= m:
                        v[i][j] = True
            for j in range(col):
                if not v[0][j] and dfs(0, j, v):
                    return True
            return False
        
        grid = [[0] * col for _ in range(row)]
        for i, (x, y) in enumerate(cells):
            grid[x-1][y-1] = i + 1
        l, r = 0, row * col
        while l < r:
            m = (l + r + 1) // 2
            v = [[False] * col for _ in range(row)]
            if check(m):
                l = m
            else:
                r = m - 1
        return l