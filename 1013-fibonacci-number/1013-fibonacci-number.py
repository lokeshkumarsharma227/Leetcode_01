class Solution:
    def fib(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        return self._fib(n, dp)
    
    def _fib(self, n: int, dp: list) -> int:
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self._fib(n - 1, dp) + self._fib(n - 2, dp)
        return dp[n]
