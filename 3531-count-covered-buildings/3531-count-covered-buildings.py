class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n + 1)
        max_col = [0] * (n + 1)
        min_row = [float('inf')] * (n + 1)
        min_col = [float('inf')] * (n + 1)
        cnt = 0

        for x, y in buildings:
            min_row[y] = min(min_row[y], x)
            max_row[y] = max(max_row[y], x)
            min_col[x] = min(min_col[x], y)
            max_col[x] = max(max_col[x], y)

        for x, y in buildings:
            if min_row[y] < x < max_row[y] and min_col[x] < y < max_col[x]:
                cnt += 1
        
        return cnt