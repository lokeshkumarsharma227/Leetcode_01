class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n=len(shifts)
        suffix_sum=[0]*n
        suffix_sum[-1]=shifts[-1]
        for i in range (n-2,-1,-1):
            suffix_sum[i]=(suffix_sum[i+1]+shifts[i])%26

        res=[]
        for i in range(len(s)):
            char = chr((ord(s[i]) - ord('a') + suffix_sum[i]) % 26 + ord('a'))
            res.append(char)

        return "".join(res)
            
            

            


        