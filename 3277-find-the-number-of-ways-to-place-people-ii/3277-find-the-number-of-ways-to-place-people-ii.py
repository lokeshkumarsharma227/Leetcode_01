class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        for j in range(len(points)):
            for i in range(len(points)-1):
                if points[i][0] > points[i+1][0]:
                    points[i], points[i+1] = points[i+1], points[i]
                elif points[i][0] == points[i+1][0]:
                    if points[i][1] < points[i+1][1]:
                        points[i], points[i+1] = points[i+1], points[i]

        for i in range(len(points)):
            arr = []
            for j in range(i+1, len(points)):
                if points[i][1] < points[j][1]:
                    continue
                c = 0
                for yVal in arr:
                    if yVal >= points[j][1]:
                        c = 1
                        break
                if c == 0:
                    arr.append(points[j][1])
                    res += 1
        return res
                
                
        