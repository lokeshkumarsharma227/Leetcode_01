class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        def countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count

        
        count=0
        while num1>0 and num1>num2:
            count+=1
            num1-=num2
            if countSetBits(num1)<=count and num1>=count:
                return count
        
        return -1
        