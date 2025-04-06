from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            key1, val1 = nums1[i]
            key2, val2 = nums2[j]

            if key1 == key2:
                merged.append([key1, val1 + val2])
                i += 1
                j += 1
            elif key1 < key2:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < n:
            merged.append(nums1[i])
            i += 1
        while j < m:
            merged.append(nums2[j])
            j += 1

        return merged
