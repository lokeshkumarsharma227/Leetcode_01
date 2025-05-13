class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (t + 1) for _ in range(26)]
        
        for ch in range(26):
            dp[ch][0] = 1
        
        for i in range(1, t + 1):
            for ch in range(26):
                if ch == 25:
                    dp[ch][i] = (dp[0][i - 1] + dp[1][i - 1]) % MOD
                else:
                    dp[ch][i] = dp[ch + 1][i - 1]
        
        total = 0
        for ch in s:
            index = ord(ch) - ord('a')
            total = (total + dp[index][t]) % MOD
        
        return total
