class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        curr=0
        for i in gain:
            curr+=i
            res=max(curr,res)

        return res

        