class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        count=1
        power=[]
        while n>0:
            if n%2==1:
                power.append(count)
            count*=2
            n = n>>1
            
        
        pre=[1]
        for i in power:
            pre.append(pre[-1]*i)
        sol=[]
        for l,r in queries:
            sol.append((pre[r+1]//pre[l]) % (10**9+7))

        return sol
