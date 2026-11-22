class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ret = []
        queens = [['.' for _ in range(n)] for _ in range(n)]

        def is_attacked(queens, row, col):
            for c in range(n):
                if c != col and queens[row][c] == 'Q':
                    return True
            
            for r in range(n):
                if r != row and queens[r][col] == 'Q':
                    return True
            
            # up-left
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if queens[r][c] == 'Q':
                    return True
                r -= 1
                c -= 1
            
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if queens[r][c] == 'Q':
                    return True
                
                r -= 1
                c += 1

        def dfs(num_queens, row, col):
            if is_attacked(queens, row, col):
                return
            if num_queens == n:
                ret.append(["".join(board_row) for board_row in queens])
                return
            
            i = row + 1
            for j in range(n):
                queens[i][j] = 'Q'
                dfs(num_queens + 1, i, j)
                queens[i][j] = '.'
        
        for j in range(n):
            queens[0][j] = 'Q'
            dfs(1, 0, j)
            queens[0][j] = '.'
        
        return ret
            
            
            