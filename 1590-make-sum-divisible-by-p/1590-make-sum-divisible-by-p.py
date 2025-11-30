class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mp={0:-1}
        sum1=0
        k=sum(nums)%p
        if k==0:
            return 0
        minlen=len(nums)
        for i in range(len(nums)):
            sum1+=nums[i]
            summod=sum1%p
            need=(summod-k+p)%p
            if need in mp:
                minlen=min(minlen,i-mp[need])
            mp[summod]=i
        if minlen==len(nums):
            return -1
        return minlen