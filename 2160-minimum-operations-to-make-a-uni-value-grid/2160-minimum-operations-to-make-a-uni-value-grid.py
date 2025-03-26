class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = []
        for r in grid:
            a.extend(r)
        a.sort()
        
        m = a[len(a) // 2]
        c = 0
        
        for v in a:
            d = abs(v - m)
            if d % x != 0:
                return -1
            c += d // x
        
        return c