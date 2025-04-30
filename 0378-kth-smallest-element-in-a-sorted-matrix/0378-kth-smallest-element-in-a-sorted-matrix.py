class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0] - 1, matrix[n-1][n-1]
        
        def condition(val):
            count = 0
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= val:
                    count += (i + 1)
                    j += 1
                else:
                    i -= 1
            return count
        
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid) >= k:
                hi = mid
            else:
                lo = mid
        
        return hi