class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        prefixsum=[0]*(len(nums))
        prefixsum[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            prefixsum[i]=nums[i]+prefixsum[i+1]
        for i in range(1,k):
            dp[i]=dp[i-1]+nums[i]
        for i in range(k,len(nums)):
            currentKsum=prefixsum[i - k + 1] - prefixsum[i]+nums[i]
            if i<2*k-1:
                dp[i] =  currentKsum
            else:
                dp[i]=max(currentKsum,dp[i-k]+currentKsum)
        return max(dp[k-1:])