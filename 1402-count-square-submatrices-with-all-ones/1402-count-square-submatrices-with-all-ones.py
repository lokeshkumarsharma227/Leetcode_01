class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        @cache
        def largest_square(i, j):
            if i < 0 or j < 0 or matrix[i][j] == 0:
                return 0
            return min(largest_square(i - 1, j - 1), 
                       largest_square(i - 1, j), 
                       largest_square(i, j - 1)) + 1
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += largest_square(i, j)
        return count