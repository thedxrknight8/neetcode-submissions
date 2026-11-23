class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        ret = float('inf')

        while q:
            # print(q.popleft())
            curr, changes = q.popleft()
            
            if curr == endWord:
                ret = min(changes, ret)
            
            for c in "abcdefghijklmaonpqrstuvwxyz":
                for i in range(len(curr)):
                    newWord = curr[:i] + c + curr[i + 1:]
                    if newWord not in visited and newWord in wordList:
                        visited.add(newWord)
                        q.append((newWord, changes + 1))
        return ret if ret != float("inf") else 0
                    