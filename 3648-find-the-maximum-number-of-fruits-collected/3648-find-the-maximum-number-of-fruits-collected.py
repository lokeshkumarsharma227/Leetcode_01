class Solution:
    def maxCollectedFruits(self, grid: List[List[int]]) -> int:
        n = len(grid)
        diagonal = sum(grid[i][i] for i in range(n))
        dp = []
        for i in range(n):
            dp.append([-inf] * n)
        dp[0][n-1] = grid[0][n-1]
        dp[n-1][0] = grid[n-1][0]
        for i in range(1, n):
            for j in range(i+1, n):
                dp[i][j] = dp[i-1][j] + grid[i][j]
                dp[j][i] = dp[j][i-1] + grid[j][i]
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1] + grid[i][j])
                    dp[j][i] = max(dp[j][i], dp[j+1][i-1] + grid[j][i])
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + grid[i][j])
                    dp[j][i] = max(dp[j][i], dp[j-1][i-1] + grid[j][i])
        return diagonal + dp[n-1][n-2] + dp[n-2][n-1]