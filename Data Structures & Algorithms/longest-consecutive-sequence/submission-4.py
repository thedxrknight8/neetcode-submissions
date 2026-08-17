class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        run_length = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                
                run_length = max(run_length, y - x)
        
        return run_length