class Solution:
    def isValidCap(self, cap, nums, k):
        robbed, canRob = 0, True
        for house in nums:
            if not canRob:
                canRob = True
            elif house <= cap:
                robbed += 1
                canRob = False
        return robbed >= k

    def minCapability(self, nums, k):
        posCaps = sorted(set(nums))
        left, right = 0, len(posCaps) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.isValidCap(posCaps[mid], nums, k):
                right = mid
            else:
                left = mid + 1
        
        return posCaps[left]
