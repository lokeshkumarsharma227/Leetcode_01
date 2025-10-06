class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def canReachEndAtTime(t: int) -> bool:
            if grid[0][0] > t:
                return False
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            while queue:
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False
        left, right = grid[0][0], n * n - 1
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canReachEndAtTime(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
