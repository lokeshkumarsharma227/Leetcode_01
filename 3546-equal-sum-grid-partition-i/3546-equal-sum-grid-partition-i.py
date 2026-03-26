class Solution:
    def canPartitionGrid(self, grid):
        def check(A):
            cur = 0
            for r in A:
                cur += sum(r)
                if cur * 2 == total:
                    return True
            return False

        total = sum(sum(r) for r in grid)

        if total % 2 != 0:
            return False

        return check(grid) or check(zip(*grid))