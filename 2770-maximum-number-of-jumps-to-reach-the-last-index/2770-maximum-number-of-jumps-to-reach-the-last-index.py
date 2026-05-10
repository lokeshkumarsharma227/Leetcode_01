class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(i):
            if i == n-1 : return 0
            
            res = -math.inf
            for ind in range(i+1,n):
                if abs(nums[i] - nums[ind]) <= target:
                    res = max(
                        res,
                        1 + solve(ind)
                    )
            return res
        
        maxSteps = solve(0)
        return maxSteps if maxSteps != -math.inf else -1