class Solution:
    def totalMoney(self, n: int) -> int:
        def week(days, n=1, wek=7):
            res = 0
            for day in range(n, days+n):
                res += day
                print(day)
                if day == wek:
                    return res + week(days-7, n+1, wek+1)
            return res
        return week(n)