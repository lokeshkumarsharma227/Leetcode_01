class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = 0, 0, 0
        start, ans, n = 0, 0, len(s)
        i = 0
        
        while i < n:
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0:
                ans += (n-i)
                if s[start] == 'a':
                    a -= 1
                elif s[start] == 'b':
                    b -= 1
                else:
                    c -= 1
                start += 1
            i += 1
        
        return ans