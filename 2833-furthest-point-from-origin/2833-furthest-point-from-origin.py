class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:


        countL = moves.count('L')
        countR = moves.count('R')
        count_ = moves.count('_')

        mx = max(countL, countR)

        mn = min(countL, countR)

        return count_+mx - mn