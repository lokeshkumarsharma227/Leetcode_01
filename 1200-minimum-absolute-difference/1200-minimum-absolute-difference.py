class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif = float('inf')
        result = []
        for i in range(1,len(arr)):
            val = abs(arr[i] - arr[i-1])
            if val < min_dif:
                result = []
                min_dif = val
                result.append([arr[i-1],arr[i]])
            elif val <= min_dif:
                result.append(([arr[i-1],arr[i]]))
        return result