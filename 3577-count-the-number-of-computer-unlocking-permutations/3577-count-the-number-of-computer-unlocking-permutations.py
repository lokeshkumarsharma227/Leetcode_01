class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        x = min(complexity[1:])
        if complexity[0] >= x:
            return 0
        
        ans = 1
        for i in range(2,len(complexity)):
            ans = ans * i % MOD
        return ans