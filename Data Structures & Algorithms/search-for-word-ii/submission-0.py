class TrieNode():
        def __init__(self): 
            self.children = {}
            self.isWord = False
        
        def addWord(self, word):
            cur = self
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = True

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        visited = set()
        res = set()
        
        def dfs(r, c, word, node):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in node.children or (r, c) in visited:
                return
            
            visited.add((r, c))
            child_node = node.children[board[r][c]]
            word += board[r][c]
            if child_node.isWord:
                res.add(word)

            dfs(r + 1, c, word, child_node)
            dfs(r, c + 1, word, child_node)
            dfs(r - 1, c, word, child_node)
            dfs(r, c - 1, word, child_node)
            visited.remove((r, c))
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", root)
    
        return list(res)
        