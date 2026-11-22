class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ret = []

        # if a cell is in both pac and atl, then they are good
        # run dfs from every cell on the borders
        # so for every cell in pac, run dfs and add every cell 
        # you can go to to pac. same thing with atl

        directions = [(0,-1), (0,1), (1,0), (-1,0)]

        def dfs(i, j, visited):
            if (i,j) in visited:
                return
            visited.add((i, j))

            for dx, dy in directions:
                row = dx + i
                col = dy + j
                if 0 <= row < len(heights) and 0 <= col < len(heights[0]) and heights[i][j] <= heights[row][col]:
                    dfs(row, col, visited) 
        
        # first, pac
        for j in range(len(heights[0])):
            dfs(0, j, pac)
        for i in range(1, len(heights)):
            dfs(i, 0, pac)
        
        # then, atl
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, atl)
        for i in range(len(heights) - 1):
            dfs(i, len(heights[0]) - 1, atl)
        
        for coord in pac:
            if coord in atl:
                ret.append([coord[0], coord[1]])
        
        return ret
 
