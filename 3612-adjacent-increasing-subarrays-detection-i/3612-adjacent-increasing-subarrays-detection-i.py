class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if k==1:
            return True
        if n < 2 * k:
            return False
        temp=[False]*n
        l,r=0,1
        while(r<n):
            while r<n and nums[r] > nums[r-1]:
                if r-l+1==k:
                    temp[l]=True
                    l+=1
                r+=1
            r+=1
            l=r-1
        i=k
        while i<n:
            if temp[i] and temp[i-k]:
                return True
            i+=1

        return False
        