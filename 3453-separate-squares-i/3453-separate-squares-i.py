def isBalanced(y: float, squares: List[List[int]]) -> bool:
    area_above = 0
    area_below = 0
    for x, bottom_y, length in squares:
        top_y = bottom_y + length
        if y >= top_y:
            area_below += length * length
        elif y <= bottom_y:
            area_above += length * length
        else:
            h_below = y - bottom_y
            h_above = length - h_below
            area_below += length * h_below
            area_above += length * h_above
    return area_above <= area_below

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        min1 = min(s[1] for s in squares)
        max1 = max(s[1] + s[2] for s in squares)
        result = max1
        while max1 - min1 > 1e-6:
            mid = (min1 + max1) / 2
            if isBalanced(mid, squares):
                result = mid
                max1 = mid
            else:
                min1 = mid
        return result
