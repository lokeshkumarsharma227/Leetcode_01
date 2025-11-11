class Solution:
    def solve(self, strs, index, m, n, dp):
        if index < 0:
            return 0
        if dp[index][m][n] != -1:
            return dp[index][m][n]
        
        zeros, ones = strs[index].count("0"), strs[index].count("1")
        if zeros <= m and ones <= n:
            dp[index][m][n] = max(1 + self.solve(strs, index - 1, m - zeros, n - ones, dp),
                                   self.solve(strs, index - 1, m, n, dp))
        else:
            dp[index][m][n] = self.solve(strs, index - 1, m, n, dp)
        
        return dp[index][m][n]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]
        return self.solve(strs, len(strs) - 1, m, n, dp)
