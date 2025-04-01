class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        t = set(s)
        ans = 0
        for c in t:
            l = s.index(c)
            r = s.rindex(c)
            res = set()
            for a in range(l + 1, r):
                res.add(s[a])
            ans += len(res)
        return ans