class Solution :
    def maxDotProduct( self, nums1 : List[int], nums2 : List[int] ) -> int :
        length = len(nums2) + 1
        dp = [float("-inf")] * (len(nums1) + 1) * length
        for index in range(1, len(nums1) + 1) :
            for jndex in range(1, length) :
                product = nums1[index - 1] * nums2[jndex - 1]
                dp[index * length + jndex] = max(
                    product + max(dp[(index - 1) * length + (jndex - 1)], 0),
                    dp[(index - 1) * length + jndex],
                    dp[index * length + (jndex - 1)]
                )
        return dp[len(nums1) * length + len(nums2)]