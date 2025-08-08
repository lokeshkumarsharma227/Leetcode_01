class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0: return 0.5
        elif n >= 4796: return 1
        n, ans = (ceil(n/25) + 4), 0
        dp = [[0]*(n) for _ in range(n)]
        dp[-1][-1] = 1
        for b in range(n-1,-1,-1):
            for a in range(n-1,-1,-1):
                if b == a == n-1: continue
                if 3 < b < n and 3 < a + 4 < n: dp[b][a] += dp[b][a+4]
                if 3 < b+1 < n and 3 < a+3 < n: dp[b][a] += dp[b+1][a+3]
                if 3 < b+2 < n and 3 < a+2 < n: dp[b][a] += dp[b+2][a+2]
                if 3 < b+3 < n and 3 < a+1 < n: dp[b][a] += dp[b+3][a+1]
                if b <= 3 and a <= 3: dp[b][a] /= 2
                dp[b][a] /= 4
        for b in range(n):
            for a in range(4):
                ans += dp[b][a]
        return ans