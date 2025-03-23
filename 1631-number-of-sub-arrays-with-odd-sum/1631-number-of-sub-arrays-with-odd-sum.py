class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count, odd_count = 1, 0  
        prefix_sum = 0
        result = 0
    
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1
        return result