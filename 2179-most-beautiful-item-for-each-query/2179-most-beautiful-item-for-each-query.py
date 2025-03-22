class Solution:
    def isPossible(self, items, mid, beauty):
        max_beauty = 0
        for price, b in items:
            if price <= mid:
                max_beauty = max(max_beauty, b)
        return max_beauty

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(queries)
        answer = [0] * n
        
        max_beauty = []
        curr_max = 0

        for price, beauty in items:
            curr_max = max(curr_max, beauty)
            max_beauty.append((price, curr_max))
        
        for i in range(n):
            cap_min, cap_max = 0, len(max_beauty) - 1
            res = 0

            while cap_min <= cap_max:
                mid = (cap_min + cap_max) // 2
                if max_beauty[mid][0] <= queries[i]:
                    res = max_beauty[mid][1]
                    cap_min = mid + 1
                else:
                    cap_max = mid - 1
            
            answer[i] = res
        
        return answer
