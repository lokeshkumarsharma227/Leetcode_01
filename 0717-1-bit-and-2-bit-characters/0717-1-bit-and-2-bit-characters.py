class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] == 1:
            count += 1
            i -= 1
        return count % 2 == 0
