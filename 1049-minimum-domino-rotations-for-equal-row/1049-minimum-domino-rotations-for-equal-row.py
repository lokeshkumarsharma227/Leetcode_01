class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = (tops[0], bottoms[0])
        top1, top2, bot1, bot2 = 0, 0, 0, 0
        dupe1, dupe2 = 0, 0
        for i in range(len(tops)):
            if tops[i] not in n and bottoms[i] not in n:
                return -1
            if tops[i] == bottoms[i] == n[0]:
                dupe1 += 1
            if tops[i] == bottoms[i] == n[1]:
                dupe2 += 1
            if tops[i] == n[0]:
                top1 += 1
            if tops[i] == n[1]:
                top2 += 1
            if bottoms[i] == n[0]:
                bot1 += 1
            if bottoms[i] == n[1]:
                bot2 += 1
        if top1 + bot1 - dupe1 >= len(tops):
            return min(top1, bot1) - dupe1
        if top2 + bot2 - dupe2 >= len(tops):
            return min(top2, bot2) - dupe2
        return -1