class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        prev: int = 0
        length: int = 0
        for num in nums:
            if prev <= num:
                prev = num
                length += 1
        return length