class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        freq = Counter(nums)
        res = max(freq.values())
        for a in freq:
            for b in [a-k,a,a+k]:
                i = bisect.bisect_left(nums,b-k)
                j = bisect.bisect_right(nums,b+k)
                M = j-i-freq[b]
                res = max(res,freq[b]+min(numOperations,M))
        return res


        