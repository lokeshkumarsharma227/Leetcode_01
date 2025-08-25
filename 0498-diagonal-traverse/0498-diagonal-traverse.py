class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        ans = []
        ans.append(mat[0][0])
        i = 0
        j = 0
        flag = 0
        while(True):
            if(flag==0):
                j+=1
                if j<n: ans.append(mat[i][j])
                
                while(i+1<m and j-1>=0):
                    ans.append(mat[i+1][j-1])
                    i+=1
                    j-=1
                    
            if(flag==1):
                i+=1
                if i<m: ans.append(mat[i][j])
                while(i-1>=0 and j+1<n):
                    ans.append(mat[i-1][j+1])
                    i-=1
                    j+=1

            flag = not flag

            if i>=m-1 and j>=n-1:
                break

        return ans