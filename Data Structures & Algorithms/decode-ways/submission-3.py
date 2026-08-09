class Solution:
    def numDecodings(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1 if s != '0' else 0
        # if len(s) == 0:
        #     return 0
        
        # def is_valid(i, j):
        #     return j - i <= 2 and s[i] != '0' and int(s[i:j + 1]) < 27
        
        # dp = [[0] * 2 for _ in range(len(s))]
        # dp[len(s) - 1][len(s) - 1] = 0 if not is_valid(len(s) - 1, len(s) - 1) else 1
        # dp[len(s) - 2][len(s) - 1] = 0 if not is_valid(len(s) - 2, len(s) - 1) else 1

        # for i in range(len(s) - 3, -1, -1):
        #     for j in range(i, len(s)):
        #         add = 0 if not is_valid(i, j) else 1
        #         dp[i][j] = add + dp[i + 1][i + 1] + dp[i + 1][i + 2]
        # return dp[0][0] 

        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                res = dp[i + 1]
                if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                    res += dp[i + 2]
                dp[i] = res
        return dp[0]

        
                