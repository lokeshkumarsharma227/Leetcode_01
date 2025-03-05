class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contain = set()
        for i in range(len(nums)):
            if nums[i] in contain:
                return True
            contain.add(nums[i])
            if len(contain) > k:
                contain.remove(nums[i - k])
        return False