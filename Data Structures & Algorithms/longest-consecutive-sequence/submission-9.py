class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)

        ret = 1
        for num in nums:
            if num - 1 not in nums:
                x = num + 1
                while x in nums:
                    x += 1
                    ret = max(ret, x - num)
        
        return ret