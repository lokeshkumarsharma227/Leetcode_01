class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxi = 0

        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    maxi = max(maxi, (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        
        return maxi