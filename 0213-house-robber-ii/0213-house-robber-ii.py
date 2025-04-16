from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_robbed_amount(coins):
            n = len(coins)
            if n == 0:
                return 0
            elif n == 1:
                return coins[0]
            
            second_last = 0
            last = coins[0]
            
            for i in range(1, n):
                ans = max(coins[i] + second_last, last)
                second_last = last
                last = ans
            
            return last
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        case1 = max_robbed_amount(nums[1:])
        case2 = max_robbed_amount(nums[:-1])
        
        return max(case1, case2)
