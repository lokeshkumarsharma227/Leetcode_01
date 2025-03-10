class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        if 1  not in nums:
            return 1
        for i in range(n):
            if nums[i]<1 or nums[i]>n:
                nums[i]=1
        for i in range(n):
            it = abs(nums[i])  
            if it<=n and nums[it-1]>0:
                nums[it - 1] = -(nums[it - 1]) 

        for i in range(n):
            if nums[i]>0 and nums[i]!=0:
                return i+1
        return n+1