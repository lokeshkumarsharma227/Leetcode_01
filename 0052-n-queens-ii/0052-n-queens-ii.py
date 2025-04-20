class Solution:
    def isQueenValid(self, board, row, col, n):
        for i in range(row):
            if board[i][col] or \
               (col - (row - i) >= 0 and board[i][col - (row - i)]) or \
               (col + (row - i) < n and board[i][col + (row - i)]):
                return False
        return True

    def Solve(self, board, n, r):
        if r == n:
            return 1
        count = 0
        for c in range(n):
            if self.isQueenValid(board, r, c, n):
                board[r][c] = True
                count += self.Solve(board, n, r + 1)
                board[r][c] = False
        return count

    def totalNQueens(self, n: int) -> int:
        board = [[False for _ in range(n)] for _ in range(n)]
        return self.Solve(board, n, 0)
