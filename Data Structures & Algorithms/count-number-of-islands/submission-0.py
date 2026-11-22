class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # whenever you come across a '1', dfs and knock out all the cells
        # adjacent manhattan that are '1'. 
        # and num_comps += 1

        num_comps = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(i, j):
            # iterate in all 4 directions and dfs on the ones that are ones
            for dx, dy in directions:
                r = dx + i
                c = dy + j
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                    grid[r][c] = '0'
                    dfs(r, c)
                      

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_comps += 1
                    grid[i][j] = '0'
                    dfs(i, j)

        return num_comps

