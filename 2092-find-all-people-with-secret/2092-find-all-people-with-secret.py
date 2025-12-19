class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        know = set([0, firstPerson])
        curTime = 0
        g = {}
        def dfs(x):
            nonlocal g
            nonlocal know
            know.add(x)
            for nei in g.get(x,[]):
                if nei not in know:
                    dfs(nei)
        for meeting in meetings:
            if curTime != meeting[2]:
                g = {}
                curTime = meeting[2]
            a, b = meeting[0], meeting[1]
            if a in know:
                dfs(b)
            elif b in know:
                dfs(a)
            else:
                g[a] = g.get(a, []) + [b]
                g[b] = g.get(b, []) + [a]
        return list(know)
            