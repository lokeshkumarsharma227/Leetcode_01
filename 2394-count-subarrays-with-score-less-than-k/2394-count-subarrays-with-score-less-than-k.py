class Solution(object):
    def countSubarrays(self, nums, k):
        count = 0
        sum1 = 0
        left = 0
        for right in range(len(nums)):
            sum1 += nums[right]
            while sum1 * (right - left + 1) >= k:
                sum1 -= nums[left]
                left += 1
            count += (right - left + 1)
        return count