class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        path = 0  # count of non-obstacle empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                if grid[i][j] == 2:
                    ei, ej = i, j
                if grid[i][j] == 0:
                    path += 1

        # Direction deltas
        directions = {
            'u': (-1, 0),
            'd': (1, 0),
            'l': (0, -1),
            'r': (0, 1)
        }

        def backtrack(x, y, path):
            if (x, y) == (ei, ej):
                return 1 if path == -1 else 0  
            temp = grid[x][y]
            grid[x][y] = -2  # mark as visited
            result = 0

            for dir in ['u', 'd', 'l', 'r']:
                dx, dy = directions[dir]
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (grid[nx][ny] == 0 or grid[nx][ny] == 2):
                    result += backtrack(nx, ny, path - 1)

            grid[x][y] = temp  # unmark
            return result

        return backtrack(si, sj, path)
