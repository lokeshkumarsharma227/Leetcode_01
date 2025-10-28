class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        t=sum(nums)
        n=len(nums)
        s=0
        ans=0
        for i in range(n):
            rs=t-s
            if(nums[i]==0):
                if(s==rs):
                    ans+=2
                elif(abs(rs-s)==1):
                    ans+=1
            s+=nums[i]
        return ans


        