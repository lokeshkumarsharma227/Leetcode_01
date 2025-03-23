class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
                if left_sum == total - nums[i] - left_sum:
                    return i
                left_sum += nums[i]
        return -1