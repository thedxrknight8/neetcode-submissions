class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add every (row, col) pair to a queue for BFS search
        # that represents a treasure chest

        # then start a queue search and append in all 4 directions 
        # of course, you need visited and you can't visit visited cells
        # visited set has structure (row, col)
        # and then for the queue, it uses (row, col, timestep)

        # then, you pop off items, and mark the grid itself with those values

        # if you come across a -1, you can't go there 
        # actually do you need a visited set?
        # you can just make sure that you are only going over INF vertices
        INF = 2147483647
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        # bfs

        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while q:
            r, c, timestep = q.popleft()

            for dx, dy in directions:
                row = dx + r
                col = dy + c

                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == INF:
                    grid[row][col] = timestep + 1
                    q.append((row, col, timestep + 1))
            
