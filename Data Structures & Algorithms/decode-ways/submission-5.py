class Solution:
    def numDecodings(self, s: str) -> int:
        # take one character OR take two characters
        
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] if s[i] != '0' else 0
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]
