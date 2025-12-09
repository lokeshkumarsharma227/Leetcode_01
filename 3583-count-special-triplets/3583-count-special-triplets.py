class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = {}
        right = {}
        for i in nums:
            right[i] = right.get(i, 0) +1
        ans = 0
        mod = 10**9 + 7
        for i in nums:
            l = left.get(i*2,0)
            right[i] -= 1
            r = right.get(i*2 ,0)
            if l >= 1 and r >= 1:
                ans = (ans + l * r) % mod
            left[i] = left.get(i, 0)+1
        return ans

        