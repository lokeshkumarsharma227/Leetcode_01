class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n - 1
        
        while a <= b:
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]
            a += 1
            b -= 1
        
        return []