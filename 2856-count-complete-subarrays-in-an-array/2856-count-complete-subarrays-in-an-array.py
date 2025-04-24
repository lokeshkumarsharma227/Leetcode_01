class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        start = 0
        end = 0
        total = 0
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        unique_required = len(set(nums))
        count = 0

        while end < len(nums):
            num_end = nums[end]
            freq[num_end] += 1

            if freq[num_end] == 1:
                count += 1

            while count == unique_required:
                total += (len(nums) - end)

                num_start = nums[start]
                freq[num_start] -= 1

                if freq[num_start] == 0:
                    count -= 1

                start += 1

            end += 1

        return total
