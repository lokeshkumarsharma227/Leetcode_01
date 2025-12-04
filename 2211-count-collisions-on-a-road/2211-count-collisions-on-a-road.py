class Solution:
    def countCollisions(self, directions: str) -> int:
        s=list(directions)
        l=len(s)
        p=s[0]
        C=0
        NR=0
        for i in range(1,l):
            if p=="L" and s[i]=="L":
                p="L"
            elif p=="L" and s[i]=="S":
                p="S"
            elif p=="L" and s[i]=="R":
                p="R"
            elif p=="S" and s[i]=="L":
                C=C+1
                p="S"
            elif p=="S" and s[i]=="S":
                p="S"
            elif p=="S" and s[i]=="R":
                p="R"
            elif p=="R" and s[i]=="L":
                if NR==0:
                    C=C+2
                    p="S"
                else:
                    C=C+NR+2
                    NR=0
                    p="S"
            elif p=="R" and s[i]=="S":
                if NR==0:
                    C=C+1
                    p="S"
                else:
                    C=C+NR+1
                    NR=0
                    p="S"
            elif p=="R" and s[i]=="R":
                p="R"
                NR=NR+1
        return C