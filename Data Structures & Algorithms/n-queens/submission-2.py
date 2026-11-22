class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # you can place a queen anywhere and backtrack from that
        # more specifically, you can place a queen on a square, and dfs
        # on that square such that you can place more queens
        # you can place a queen anywhere that has a dot
        # and of course, isn't attacked by another queen

        # you use the same grid everytime, just remove whenever you backtrack
        # backtrack means placing a dot instead of a Q
        # you can potentially place a queen on any square so you 
        # need to iterate through every square

        # but you can start at a particular square in the dfs, you don't 
        # have to restart and start placing at (0, 0)

        # and when the # of queens placed (through a tracker) = n, 
        # add to ret

        # final question: how would you check if queens can attack? 
        # you check the row, then you check the col, then you check the diagonals -> for i, j: i + 1, j + 1 | for i, j: i - 1, j - 1

        ret = []
        queens = [['.' for _ in range(n)] for _ in range(n)] 

        def is_attacked(queens, row, col):
            for j in range(n):
                if j != col and queens[row][j] == 'Q':
                    return True
            
            for i in range(n):
                if i != row and queens[i][col] == 'Q':
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
            
            return False

        def dfs(num_queens, row, col):
            if is_attacked(queens, row, col):
                return
            if num_queens == n:
                ret.append(["".join(board_row) for board_row in queens])
                return
            
            # you should iterate starting from the next row
            i = row + 1
            for j in range(n):
                if queens[i][j] == '.':
                    queens[i][j] = 'Q'
                    dfs(num_queens + 1, i, j)
                    queens[i][j] = '.'
        
        for j in range(n):
            queens[0][j] = 'Q'
            dfs(1, 0, j)
            queens[0][j] = '.'

        return ret
            