from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 not in nums:
            return 1

        for i in range(n):
            if nums[i] < 1 or nums[i] > n:  
                nums[i] = 1  

        for i in range(n):
            it = abs(nums[i])
            if 1 <= it <= n:  
                nums[it - 1] = -abs(nums[it - 1])  

        for i in range(n):
            if nums[i] > 0:  
                return i + 1

        return n + 1
