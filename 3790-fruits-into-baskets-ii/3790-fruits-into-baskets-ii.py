class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for i in range(len(fruits)):
            placed = False
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = -1  
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced