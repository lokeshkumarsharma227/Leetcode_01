class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in ans:
                return [ans[b],i]
            ans[nums[i]]=i
        
