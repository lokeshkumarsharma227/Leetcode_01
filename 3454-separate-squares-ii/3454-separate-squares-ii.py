class Solution:
    def separateSquares(self, squares):
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        active = []
        prev_y = events[0][0]
        slices = []
        total_area = 0

        def union_width(intervals):
            intervals.sort()
            w = 0
            right = -10**30
            for l, r in intervals:
                if l > right:
                    w += r - l
                    right = r
                elif r > right:
                    w += r - right
                    right = r
            return w

        for y, t, xl, xr in events:
            if y > prev_y and active:
                h = y - prev_y
                w = union_width(active)
                slices.append((prev_y, h, w))
                total_area += h * w

            if t == 1:
                active.append((xl, xr))
            else:
                active.remove((xl, xr))

            prev_y = y

        half = total_area / 2
        cur = 0

        for sy, h, w in slices:
            if cur + h * w >= half:
                return sy + (half - cur) / w
            cur += h * w

        return float(prev_y)