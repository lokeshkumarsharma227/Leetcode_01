class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        vis = set()
        m, n = len(h), len(h[0])
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        def bfs(points: list) -> set:
            vis = set(points)
            queue = deque(points)
            add, append, popleft = vis.add, queue.append, queue.popleft

            while queue:
                x, y = popleft()

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and h[nx][ny] >= h[x][y]:
                        add((nx, ny))
                        append((nx, ny))

            return vis

        atlantic_points = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
        pacific_points = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]

        vis_a = bfs(atlantic_points)
        vis_p = bfs(pacific_points)

        return [[x, y] for x, y in vis_a & vis_p]


            