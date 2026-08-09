class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # start off from i at the end
        # for every i, go through the wordDict and find dp[i + k]
        # where k is len(word for every word in wordDict)
        # dp[i] = OR for every dp[i + k] possible
        # at the end, return dp[0]

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                w = len(word)
                if i + w < len(s) + 1 and s[i: i + w] == word:
                    dp[i] = dp[i] or dp[i + w]
        return dp[0]


        
