class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        nums.sort()
        counter = Counter(nums)

        def findFreq(num):
            left = bisect.bisect_left(nums, num - k)
            right = bisect.bisect_right(nums, num + k)

            return min(right - left, numOperations + counter[num])


        events = set()
        for num in nums:
            events.add(num - k)
            events.add(num)
            events.add(num + k)
        
        maxFreq = 1
        for num in sorted(list(events)):
            maxFreq = max(maxFreq, findFreq(num))
        
        return maxFreq