class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # visualize --- 
        # with 1 you can go to either 2,3,4
        # with 2 you can go to either 3,4
        # with 3 you can go to 4

        # make a subproblem
        # 
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]