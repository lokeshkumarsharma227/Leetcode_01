class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val==".":
                    continue

                box_val=(i//3,j//3)

                if (val in rows[i] or
                    val in cols[j] or
                    val in squares[box_val]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[box_val].add(val)
        
        return True