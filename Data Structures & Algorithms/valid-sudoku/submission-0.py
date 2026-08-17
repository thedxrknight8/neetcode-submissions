class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        squares = [[set() for _ in range(len(board[0]) // 3)] for _ in range(len(board) // 3)] 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i // 3][j // 3]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i // 3][j // 3].add(board[i][j])
        
        return True 

        