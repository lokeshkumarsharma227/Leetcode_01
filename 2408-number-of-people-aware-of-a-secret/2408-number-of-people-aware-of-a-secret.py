class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp = [0] * n
        dp[0], ct = 1, 0

        for i in range(1, n):

            dp[i] = ct + dp[i-delay] - dp[i-forget]
            ct = dp[i]

        return sum(dp[n-forget:]) % 1_000_000_007