class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 in (0, 2, 4, 5, 6, 8):
            return -1
        num = 1
        len_num = 1
        while True:
            if num % k == 0:
                return len_num
            num = (num*10 + 1) % k
            len_num += 1