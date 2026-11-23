class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2

        dp = [False] * (half + 1)

        dp[0] = True
    
        for num in nums:
            for size in range(half, num - 1, -1):
                dp[size] = dp[size] or dp[size - num]
        
        return dp[half]