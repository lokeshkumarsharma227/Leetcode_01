class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k - 1 + maxPts <= n:
            return 1.0

        dp = [1.0] + [0.0] * n
        window_sum = 1.0
        
        for point in range(1, n + 1):
            dp[point] = window_sum / maxPts
            if point < k:
                window_sum += dp[point]
            if point >= maxPts:
                window_sum -= dp[point - maxPts]
        return sum(dp[k:])
