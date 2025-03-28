class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        freq = Counter()
        window = []

        for i in range(n):
            if nums[i] < 0:
                bisect.insort(window, nums[i])
                freq[nums[i]] += 1
            
            if i >= k:
                outgoing = nums[i - k]
                if outgoing < 0:
                    freq[outgoing] -= 1
                    if freq[outgoing] == 0:
                        del freq[outgoing]
                    idx = bisect.bisect_left(window, outgoing)
                    if idx < len(window) and window[idx] == outgoing:
                        window.pop(idx)

            if i >= k - 1:
                result.append(window[x - 1] if len(window) >= x else 0)

        return result