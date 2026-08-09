class Solution:
    def rob(self, nums: List[int]) -> int:
        # same principle applies with the house adjacent. you can only rob
        # the house nearby if you don't rob the house nearby
        # what is the base case however? start from n - 1 where n = len(nums) - 1
        # (start from the second to last element)
        # no, you just have the max of the entire dp where dp[i] is the maximum you 
        # can rob at that point

        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))

        