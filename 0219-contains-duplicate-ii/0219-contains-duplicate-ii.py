class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}
        for i in range(len(nums)):
            if nums[i] in dup:
                if i - dup[nums[i]] <= k:
                    return True
            dup[nums[i]] = i
        return False
