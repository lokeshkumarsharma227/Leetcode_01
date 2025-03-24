class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res

        min1, max1 = 0, len(nums) - 1

        while min1 <= max1:
            mid = (min1 + max1) // 2
            if nums[mid] == target:
                res[0] = res[1] = mid
                lo, hi = mid - 1, mid + 1
                while lo >= 0 and nums[lo] == target:
                    res[0] = lo
                    lo -= 1
                while hi < len(nums) and nums[hi] == target:
                    res[1] = hi
                    hi += 1
                return res
            elif nums[mid] < target:
                min1 = mid + 1
            else:
                max1 = mid - 1

        return res
