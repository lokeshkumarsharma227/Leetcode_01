from typing import List

class Solution:
    def isValid(self, nums: List[int], k: int, mid: int) -> bool:
        curr_sum = 0
        Student = 1
        for n in nums:  
            curr_sum += n
            if curr_sum > mid:  
                Student += 1
                curr_sum = n
                if Student > k:
                    return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        min1, max1 = max(nums), sum(nums)
        while min1 < max1:
            mid = (min1 + max1) // 2
            if self.isValid(nums, k, mid):
                max1 = mid
            else:
                min1 = mid + 1
        
        return min1
