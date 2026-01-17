class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        size, ans = len(bottomLeft), 0
        for i in range(size-1):
            bi, ti = bottomLeft[i], topRight[i]
            for j in range(i+1, size):
                bj, tj = bottomLeft[j], topRight[j]
                overlapX = min(tj[0],ti[0]) - max(bj[0],bi[0])
                overlapY = min(tj[1],ti[1]) - max(bj[1],bi[1])
                if overlapX > 0 and overlapY > 0:
                    ans = max(ans, min(overlapX, overlapY))
        return ans*ans