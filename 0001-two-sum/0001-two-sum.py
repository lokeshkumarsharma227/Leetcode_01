class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        
        for i in range(len(nums)):
            a=nums[i]
            b=target-a
            if b in ans:
                return [ans[b],i]
            ans[a]=i
        
