class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        def helper(grid):
            r, c = len(grid), len(grid[0])
            dp1 = [[1 if grid[j][i] != 1 else 0  for i in range(c)] for j in range(r)]
            for i in range(r - 2, -1, -1):
                for j in range(c - 1, 0, -1):
                    if grid[i][j] != 1:
                        if grid[i][j] == 0:
                            dp1[i][j] = 1 + (dp1[i + 1][j - 1] if grid[i + 1][j - 1] == 2 else 0)
                        else:
                            dp1[i][j] = 1 + (dp1[i + 1][j - 1] if grid[i + 1][j - 1] == 0 else 0)
            dp2 = [[dp1[j][i]  for i in range(c)] for j in range(r)]
            for i in range(r - 2, -1, -1):
                for j in range(c - 2, -1, -1):
                    if grid[i][j] != 1:
                        if grid[i][j] == 0:
                            dp2[i][j] = max(dp2[i][j], 1 + (dp2[i + 1][j + 1] if grid[i + 1][j + 1] == 2 else 0))
                        else:
                            dp2[i][j] = max(dp2[i][j], 1 + (dp2[i + 1][j + 1] if grid[i + 1][j + 1] == 0 else 0))
            ans = 0 if count == 0 else 1
            for i in range(r - 2, -1, -1):
                for j in range(c - 2, -1, -1):
                    if grid[i][j] == 1 and grid[i + 1][j + 1] == 2:
                        ans = max(ans, 1 + dp2[i + 1][j + 1])
            return ans
        
        def rotate(matrix):
            return [list(row) for row in zip(*matrix[::-1])]
        
        count = 0
        mx = 0
        for i in grid:
            for j in i:
                if j == 1:
                    mx = 1
                    break
        for i in range(4):
            mx = max(mx, helper(grid))
            grid = rotate(grid)
        return mx
