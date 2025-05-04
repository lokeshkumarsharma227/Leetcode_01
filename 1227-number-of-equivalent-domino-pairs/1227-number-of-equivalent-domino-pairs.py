class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            t = a*10 + b if a < b else b*10 + a
            ans += d[t]
            d[t] += 1
        return ans