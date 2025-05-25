class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                r = dp[i][j+1]
                b = dp[i+1][j]
                dp[i][j] = r + b
        
        return dp[0][0]
