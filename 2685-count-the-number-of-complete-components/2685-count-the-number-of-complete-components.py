from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        adj2 = {}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        for i in range(n):
            # add the node itself
            adj[i].append(i)
            adj[i].sort()
            adj2[i] = tuple(adj[i])
        
        res = 0
        for k, v in Counter(adj2.values()).items():
            res += 1 if len(k) == v else 0
        
        return res
        
            
        
        