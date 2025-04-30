import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n.sort()
        m=len(n)
        if(m%2==0):
            a=(n[(m//2)-1]+n[math.floor((m+1)/2)])/2
        else:
            a=n[m//2]
        return a        