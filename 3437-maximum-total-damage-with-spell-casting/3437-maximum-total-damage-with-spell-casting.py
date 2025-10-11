class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        n, i = len(power), 0
        dp = [0]*(n+1)

        while i<n:
            count = 1
            p = power[i]
            while i<n-1 and p==power[i+1]:
                dp[i+1] = dp[i]
                i+=1
                count+=1

            prev_idx = bisect_right(power, p-3)
            dp[i+1] = max(dp[prev_idx]+p*count, dp[i])
            i+=1
        
        return dp[n]