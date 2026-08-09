class Solution:
    def numSquares(self, n: int) -> int:
        # another knapsack problem
        # have an array that marks up to n + 1
        # where dp[i] = the least number of perfect square numbers that sum
        # to n
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 3
        # dp[4] = 1
        # dp[5] = 2
        # dp[6] = 3 = 1 + min(dp[n - all perfect squares up to n]) = 1 + min(2, 2) = 3

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            j = 1
            min_squares = float('inf')
            while j * j <= i:
                print(j * j)
                min_squares = min(dp[i - j * j], min_squares)
                j += 1
            dp[i] = min_squares + 1
        return dp[n]