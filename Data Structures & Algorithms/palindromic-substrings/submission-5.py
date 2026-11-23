class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        count = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif j - i == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if dp[i + 1][j - 1] and s[i] == s[j] else 0
                count += dp[i][j]


        return count