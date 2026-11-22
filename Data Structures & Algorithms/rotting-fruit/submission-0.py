class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # everything next to rotten fruit, mark and then enqueue 
        # adjacent neighbors
        # and then return the steps 
        q = deque()

        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh_count += 1
            
        # only bfs over 1's

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        time_taken = 0

        while q: 
            r, c, t = q.popleft()

            time_taken = t

            for dx, dy in directions:
                row = dx + r
                col = dy + c

                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    fresh_count -= 1
                    grid[row][col] = 2
                    q.append((row, col, t + 1))
        
        return time_taken if fresh_count == 0 else -1

            