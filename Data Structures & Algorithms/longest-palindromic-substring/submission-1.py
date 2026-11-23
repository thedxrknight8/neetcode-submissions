class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can remember whether two particular indices were a palindrome
        # so for instance, dp[i][j] = True means that the string between
        # i and j (inclusive) is a palindrome

        # so then dp[i][j] = s[i] == s[j] AND dp[i + 1][j - 1]
        # dp[i][j] = True where i == j

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        ret_string = ""
        ret_len = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > ret_len:
                    ret_len = j - i + 1
                    ret_string = s[i:j + 1]
        
        return ret_string