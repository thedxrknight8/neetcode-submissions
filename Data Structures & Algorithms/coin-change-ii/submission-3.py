class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[amount][coins starting index] 
        # dp[amount][coin] = dp[amount][i + 1] + dp[amount - coins[i]][i]

        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        coins.sort()
        for i in range(len(coins)):
            dp[0][i] = 1
        
        for i in range(amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                
                if i - coins[j] >= 0:
                    dp[i][j] = dp[i][j + 1] + dp[i - coins[j]][j]
        
        return dp[amount][0]