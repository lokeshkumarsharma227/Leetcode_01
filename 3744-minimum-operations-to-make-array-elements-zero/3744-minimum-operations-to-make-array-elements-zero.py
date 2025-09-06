class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for q in queries:
            l, r = q
            n = 4
            i=1
            cur = 0
            while n <= r:
                if n-1 >=l:
                    cur += (n - 1 - l + 1) * i
                    l=n
                n*=4
                i+=1
            cur += (r - l + 1) * i
            res+=ceil(cur /2)
        return res