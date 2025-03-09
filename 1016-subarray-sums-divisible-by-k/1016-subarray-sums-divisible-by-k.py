class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = [0] * k  
        freq[0] = 1  
        
        count = 0
        sum1 = 0

        for num in nums:
            sum1 += num
            rem = sum1 % k

            if rem < 0:  
                rem += k

            count += freq[rem]  
            freq[rem] += 1  

        return count