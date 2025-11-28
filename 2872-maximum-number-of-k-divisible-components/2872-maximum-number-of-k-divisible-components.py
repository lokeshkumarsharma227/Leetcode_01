class Solution:
    def DFS(self, G, values, node, parent, k):
        s = values[node]
        for child in G[node]:
            if child != parent:
                s += self.DFS(G, values, child, node, k)
        
        if s % k == 0:
            self.res += 1
        
        return s

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.res = 0
        G = [[] for _ in range(n)]
        
        for edge in edges:
            u, v = edge[0], edge[1]
            G[u].append(v)
            G[v].append(u)
        
        self.DFS(G, values, 0, -1, k)
        
        return self.res