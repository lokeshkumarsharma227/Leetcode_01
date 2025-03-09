class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        unique = []
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, val in d.items():
            if val == 1:
                unique.append(key)
        for i in range(len(unique)):
            if i == k - 1:
                return unique[i]
        return ""