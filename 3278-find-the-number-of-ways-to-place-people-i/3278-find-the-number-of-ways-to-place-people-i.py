class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        result = 0
        points = sorted(points)

        for i in range(len(points)):
            for j in range(len(points)):

                if i != j:
                    x1 , y1 = points[i]
                    x2 , y2 = points[j]

                    if x1 <= x2 and y1 >= y2:

                        count = 0
                        for k in range(len(points)):

                            if k != i and k != j:

                                x , y = points[k]

                                if x1 <= x <= x2 and y2 <= y <= y1:
                                    count = count + 1
                                    break
                                
                        if count == 0:
                            result = result + 1

        return result