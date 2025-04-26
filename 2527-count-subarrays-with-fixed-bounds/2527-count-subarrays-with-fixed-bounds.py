class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        minPos = maxPos = -1
        outOfBound = -1

        for right in range(n):
            if nums[right] < minK or nums[right] > maxK:
                outOfBound = right
            if nums[right] == minK:
                minPos = right
            if nums[right] == maxK:
                maxPos = right
            validStart = min(minPos, maxPos)
            if validStart > outOfBound:
                count += validStart - outOfBound

        return count
