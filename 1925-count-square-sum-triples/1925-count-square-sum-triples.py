class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = floor(sqrt(a * a + b * b + 1))
                res += c <= n and c * c == a * a + b * b
        return res