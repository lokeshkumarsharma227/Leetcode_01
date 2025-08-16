class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        k = 1
        for n in str(num):    
            if k and n == '6':
                ans+='9'
                k -= 1
            else:
                ans+=n
        return int(ans)
