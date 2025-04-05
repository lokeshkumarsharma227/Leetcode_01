class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i: int, xor_sum: int) -> int:
            if i == len(nums):
                return xor_sum
            take = dfs(i + 1, xor_sum ^ nums[i])
            skip = dfs(i + 1, xor_sum)
            return take + skip

        return dfs(0, 0)