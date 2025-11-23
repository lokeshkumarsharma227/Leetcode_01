class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp: list[int] = [0, float('-inf'), float('-inf')]
        for num in nums:
            next_dp: list[int] = dp.copy()
            for i in range(3):
                next_dp[(i + num % 3) % 3] = max(next_dp[(i + num % 3) % 3], dp[i] + num)
            dp = next_dp
        return dp[0]