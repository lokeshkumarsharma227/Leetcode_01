class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        last_seen_reversed = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            if num in last_seen_reversed:
                min_dist = min(min_dist, j - last_seen_reversed[num])
                
            rev = int(str(num)[::-1])
            last_seen_reversed[rev] = j
            
        if min_dist != float('inf'):
            return min_dist
        else:
            return -1