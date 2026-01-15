class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest_consecutive(arr):
            if not arr:
                return 1

            arr.sort()
            longest = 1
            current = 1

            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1

            return longest + 1

        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)

        side = min(max_h, max_v)
        return side * side