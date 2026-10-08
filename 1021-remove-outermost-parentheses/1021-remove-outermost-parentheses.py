class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=0
        r=""
        for i in  s:
            if i=='(':
                a+=1
                if a>1:
                    r+=i
            else:
                a-=1
                if a>0:
                    r+=i
        return r


