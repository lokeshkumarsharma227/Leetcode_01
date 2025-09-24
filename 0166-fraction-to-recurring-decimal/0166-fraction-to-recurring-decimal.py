class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        n, d = abs(numerator), abs(denominator)
        res.append(str(n // d))
        r = n % d
        if r == 0:
            return "".join(res)
        res.append(".")
        seen = {}
        while r:
            if r in seen:  
                res.insert(seen[r], "(")
                res.append(")")
                break
            seen[r] = len(res)
            r *= 10
            res.append(str(r // d))
            r %= d
        return "".join(res)