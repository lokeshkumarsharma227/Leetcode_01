class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        num_bits = s = r = 0
        while s << 1 >> k == 0:
            num_bits = num_bits << 1 | 1
            mask = ~(-1 << num_bits)
            s, r = ((r ^ mask) << 1 | 1) << num_bits | s, (r << 1 | 1) << num_bits | s ^ mask
        return chr(s << 1 >> k & 1 | 48)