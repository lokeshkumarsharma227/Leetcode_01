class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = 0

        for i in range(len(colors)):
                
            if colors[i] != colors[0] :
                maxDist = max(maxDist , i)

            if colors[i] != colors[len(colors) - 1]:
                maxDist = max(maxDist , len(colors) - 1 - i)

        return maxDist
