
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        A = [1] * n 
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                A[i] = A[i - 1] + 1  
        
        left, right = 1, n // 2
        max_k = 0
        
        while left <= right:
            k = (left + right) // 2
            found = False
            
            
            for i in range(k, n):
                if A[i] >= k and A[i - k] >= k:
                    found = True
                    break
            
            if found:
                max_k = k
                left = k + 1
            else:
                right = k - 1

        return max_k
