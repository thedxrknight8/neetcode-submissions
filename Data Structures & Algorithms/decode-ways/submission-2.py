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

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            # check if the character s[i] is valid by itself, the only way 
            # it is not if the actual character is just zero
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                res += dfs(i + 2) # this is only for character check of taking a substring of multiple characters
                # basically, you are allowed either an extension of just one character (the current character you are on)
                # or taking the substring of the character + 2, which means that you took two characters
                # and it was valid
            dp[i] = res
            return dp[i]
        
        return dfs(0)
                