class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        maxVow, maxCon = 0, 0
        for car in set(s):
            if car in 'aeiou':
                if s.count(car) > maxVow:
                    maxVow = s.count(car)
            else:
                if s.count(car) > maxCon:
                    maxCon = s.count(car)
        return maxVow + maxCon