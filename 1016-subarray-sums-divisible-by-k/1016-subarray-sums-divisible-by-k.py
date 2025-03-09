class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = {0: 1}  
        count = 0
        sum1 = 0

        for i in nums:
            sum1 += i
            rem = sum1 % k
            if rem < 0:  
                rem += k

            if rem in mp:
                count += mp[rem]  
                mp[rem] += 1  
            else:
                mp[rem] = 1  

        return count