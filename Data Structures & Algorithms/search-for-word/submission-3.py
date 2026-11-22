class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # you can have a dfs start when you the character matches the first character of `word`
        # then iterate in all 4 directions but have a used set to make sure you aren't reusing
        # cells

        # you pass in the current word + current cell into the next dfs function
        # and if it matches the word, then you return true otherwise false and you try more

        # you can use `i` to indicate which index of the word you are comparing
        # to make sure that if you add caa instead of cat or even ca vs cd, then you 
        # can return immediately

        used = set()

        def dfs(i, curr, row, col):
            if curr == word:
                return True
            
            if word[i] != board[row][col]:
                return False

            
            # go in all 4 directions
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            ret = False

            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col

                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and (new_row, new_col) not in used:
                    used.add((new_row, new_col))
                    ret |= dfs(i + 1, curr + board[new_row][new_col], new_row, new_col)
                    used.remove((new_row, new_col))
            return ret

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used.add((i, j))
                    if dfs(0, word[0], i, j):
                        return True
                    used.remove((i, j))
        
        return False

        