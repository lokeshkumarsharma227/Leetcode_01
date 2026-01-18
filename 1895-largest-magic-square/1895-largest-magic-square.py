class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_pref = [[0] * (n + 1) for _ in range(m)]
        col_pref = [[0] * (m + 1) for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                row_pref[r][c+1] = row_pref[r][c] + grid[r][c]
                col_pref[c][r+1] = col_pref[c][r] + grid[r][c]

        def is_magic(r, c, k):
            target = row_pref[r][c + k] - row_pref[r][c]

            for i in range(r + 1, r + k):
                if row_pref[i][c + k] - row_pref[i][c] != target:
                    return False
            
            for j in range(c, c + k):
                if col_pref[j][r + k] - col_pref[j][r] != target:
                    return False

            diag1 = 0
            for i in range(k):
                diag1 += grid[r + i][c + i]
            if diag1 != target:
                return False
                
            diag2 = 0
            for i in range(k):
                diag2 += grid[r + i][c + k - 1 - i]
            return diag2 == target

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1
        