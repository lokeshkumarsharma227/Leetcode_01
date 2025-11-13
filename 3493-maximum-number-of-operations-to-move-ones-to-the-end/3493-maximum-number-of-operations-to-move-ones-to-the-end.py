class Solution:
    def maxOperations(self, s: str) -> int:
        n=len(s)
        res=0
        i=0
        c1=0
        while i<n:
            if s[i]=="0":
                i+=1
                continue
            if s[i-1]=="0" and s[i]=="1":
                res+=c1
            if s[i]=="1":
                c1+=1
            i+=1
        if s[i-1]=="0" and i==n:
            res+=c1
        return res