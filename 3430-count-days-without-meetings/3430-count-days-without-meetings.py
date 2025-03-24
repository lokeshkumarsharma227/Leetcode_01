class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        meetings.sort()
        
        r = []
        s, e = meetings[0]
        
        for i, j in meetings[1:]:
            if i <= e + 1:
                e = max(e, j)
            else:
                r.append([s, e])
                s, e = i, j
        r.append([s, e])
        
        c = 0
        for i, j in r:
            c += j - i + 1
        
        return days - c