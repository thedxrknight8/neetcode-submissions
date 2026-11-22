class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r, c):
            total = 1
            for dx, dy in directions:
                row = dx + r
                col = dy + c

                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    grid[row][col] = 0
                    total += dfs(row, col)
            return total
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = dfs(i, j)
                    print(res)
                    max_area = max(res, max_area)
        
        return max_area
            