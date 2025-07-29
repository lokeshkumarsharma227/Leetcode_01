class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        bit_reach = [-1] * 32  

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if (nums[i] >> bit) & 1:
                    bit_reach[bit] = i

            valid_positions = [pos for pos in bit_reach if pos != -1]

            if valid_positions:
                max_needed = max(valid_positions)
            else:
                max_needed = i

            res[i] = max_needed - i + 1

        return res