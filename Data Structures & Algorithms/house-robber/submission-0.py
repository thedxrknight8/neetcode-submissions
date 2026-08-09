class Solution:
    def rob(self, nums: List[int]) -> int:
        # you can either rob the current one and add to the dp[i - 2]
        # or you can skip by just taking dp[i - 1]
        # dp(i) = 'what is the maximum value you can rob up to the ith house?'

        memo = {}

        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            return memo[i]
        
        return dp(len(nums) - 1)