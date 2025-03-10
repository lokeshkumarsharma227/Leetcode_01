class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            it = abs(nums[i])
            if 1 <= it <= n and nums[it - 1] > 0:
                nums[it - 1] = -abs(nums[it - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1