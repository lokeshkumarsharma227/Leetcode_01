class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        second_last = 0
        last = nums[0]
        
        for i in range(1, n):
            ans = max(nums[i] + second_last, last)
            second_last = last
            last = ans
        
        return last
