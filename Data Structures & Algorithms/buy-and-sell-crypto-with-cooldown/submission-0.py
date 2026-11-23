class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at a certain point, you can either buy or sell 
        # if you sell, you have to consider i + 2

        # you can represent dp[i = index][bool = are you holding?]

        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for holding in [True, False]:
                if holding:
                    # you can either sell or hold
                    sell = dp[i + 2][False] + prices[i] if i + 2 < len(prices) else prices[i]
                    hold = dp[i + 1][True] if i + 1 < len(prices) else 0
                    dp[i][True] = max(sell, hold)
                else:
                    buy = dp[i + 1][True] - prices[i] if i + 1 < len(prices) else -prices[i]
                    hold = dp[i + 1][False] if i + 1 < len(prices) else 0
                    dp[i][False] = max(buy, hold)
        
        return dp[0][False]

