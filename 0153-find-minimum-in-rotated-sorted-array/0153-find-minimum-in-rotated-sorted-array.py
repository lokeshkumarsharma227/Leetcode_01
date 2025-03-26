class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            
            mid = (low + high) // 2
            ans = min(ans, nums[mid])
            
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return ans
