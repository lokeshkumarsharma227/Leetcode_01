class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat[0])
        count = [0]*n
        for i in range(len(mat)):
            pos = sum(mat[i])
            for j in range(n):
                if mat[i][j] == 1:
                    count[j] = count[j]+1 if pos == 1 else count[j]+2
        for i in count:
            if i == 1:
                result+=1
        return result