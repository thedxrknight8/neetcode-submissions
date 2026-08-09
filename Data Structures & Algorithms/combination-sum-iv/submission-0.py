class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return dp[target] such that dp[i] = number of ways to 
        # sum up to i using values in nums

        # simple knapsack solution
        # dp[i] = 1 + dp[i - num]

        # dp[0] = 1
        # dp[1] = 1 
        # dp[2] = 0 + 1 + 1 = 2
        # dp[3] = dp[2] + dp[1] + dp[0] = 2 + 1 + 1 = 4
        # dp[4] = dp[1] + dp[3] + dp[2] = 2 + 4 + 1 = 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]