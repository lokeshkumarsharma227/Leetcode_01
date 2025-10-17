class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        n = len(s)
        
        helper = lambda x: ord(x) - 97
        
        @cache
        def dp(i, used, mask):
            if i == n:
                return 1
                
            if used:
                if (mask | (1 << helper(s[i]))).bit_count() > k:
                    return 1 + dp(i+1, used, 1 << helper(s[i]))
                else:
                    return dp(i+1, used, mask | (1 << helper(s[i])))
                
            
            ans = 0
            for j in range(26):
                new_used = (j != helper(s[i]))
                if (mask | (1 << j)).bit_count() > k:
                    ans = max(ans, 1 + dp(i+1, new_used, 1 << j))
                else:
                    ans = max(ans, dp(i+1, new_used, mask | (1 << j)))
            
            return ans
                
                
        return dp(0, False, 0)