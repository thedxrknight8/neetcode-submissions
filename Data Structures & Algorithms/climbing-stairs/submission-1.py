class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        # top-down
        def dp(step):
            if step == 0 or step == 1:
                return 1
            
            return dp(step - 1) + dp(step - 2)
        return dp(n)

