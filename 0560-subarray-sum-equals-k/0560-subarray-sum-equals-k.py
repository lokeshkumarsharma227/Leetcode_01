class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        ans = 0
        sum1=0
        for num in nums:
            sum1 += num
            if (sum1 - k) in mp:
                ans += mp[sum1 - k]
            mp[sum1] = mp.get(sum1, 0) + 1
        
        return ans
