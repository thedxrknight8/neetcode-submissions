class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # take some cell 'o'. if connected to an 'x', you can make it an 
        # 'x' unless that cell is on the edge of the board
        # so take an 'o' you find in the middle. 
        # if 'o' is connected to an x, surround it. to add other 'o' cells
        # you must ensure they are 'o', and they aren't on the edge

        q = deque()
        safe = set()

        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    safe.add((i, j))
                    q.append((i, j))

        for j in [0, len(board[0]) - 1]:
            for i in range(len(board)):
                if board[i][j] == 'O':
                    safe.add((i, j))
                    q.append((i, j))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            r, c = q.popleft()
        
            for dx, dy in directions:
                row = r + dx
                col = c + dy

                if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O' and (row, col) not in safe:
                    safe.add((row, col))
                    q.append((row, col))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in safe:
                    # if connected to at least one x
                    board[i][j] = 'X'