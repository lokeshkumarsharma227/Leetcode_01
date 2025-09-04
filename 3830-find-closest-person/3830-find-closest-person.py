class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        if x >= z:
            dx = x - z
        else:
            dx = z - x

        if y >= z:
            dy = y - z
        else:
            dy = z - y

        if dx == dy:
            return 0
        return 1 if dx < dy else 2
