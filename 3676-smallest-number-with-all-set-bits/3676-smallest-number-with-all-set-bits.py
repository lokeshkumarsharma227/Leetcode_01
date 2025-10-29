class Solution:
    def smallestNumber(self, n: int) -> int:
        output = 0
        bit = 1

        while n>0:
            output += bit
            bit *= 2
            n = n//2

        return output
        