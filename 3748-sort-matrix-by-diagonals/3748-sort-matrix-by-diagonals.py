class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def isValid(a, b):
            return 0 <= a < n and 0 <= b < n
        for i in range(n):
            ci, cj = i, 0
            temp = []
            while isValid(ci, cj):
                temp.append(grid[ci][cj])
                ci += 1
                cj += 1
            temp.sort()
            ci, cj = i, 0
            while temp:
                grid[ci][cj] = temp.pop()
                ci += 1
                cj += 1
        for j in range(1, n):
            ci, cj = 0, j
            temp = []
            while isValid(ci, cj):
                temp.append(grid[ci][cj])
                ci += 1
                cj += 1
            temp.sort(reverse = True)
            ci, cj = 0, j
            while temp:
                grid[ci][cj] = temp.pop()
                ci += 1
                cj += 1
        return grid