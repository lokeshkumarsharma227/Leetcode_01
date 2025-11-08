class Solution:
    def minimumOneBitOperations(self, n: int) -> int: 
        pos = 0 
        t = True 
        c = 1 
        while n > 0 :
            if n &1 == 1 :
                if t  : 
                    pos += (int(2**c)) -1
                else : 
                    pos -= (int( pow (2,c) ) -1)
                t = not t
            n>>=1 
            c+=1  
        return abs(pos) 
                