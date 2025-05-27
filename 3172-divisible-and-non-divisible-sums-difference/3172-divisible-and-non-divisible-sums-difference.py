class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans=0
        divisible=[]
        not_divisible=[]
        divisible_sum=0
        not_divisible_sum=0
        for i in range(1,n+1):
            if i%m!=0:
                not_divisible.append(i)
            else:
                divisible.append(i)
        divisible_sum=sum(divisible)
        not_divisible_sum=sum(not_divisible)
        ans=not_divisible_sum-divisible_sum
        return ans
