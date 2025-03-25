class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min1=0
        max1=len(nums)-1
        for i in nums:
            mid=min1+(max1-min1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                min1=mid+1
            else:
                max1=mid-1
        return -1