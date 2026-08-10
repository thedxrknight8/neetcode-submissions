class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply the left part with the right part
        # but how to do without extra space? 
        # start with left value and the right value
        # like left = 1
        # right = 48
        # left * right = i
        # left *= curr
        # right /= curr
        # i += 1
        # 

        left = [1] * len(nums)
        right = [1] * len(nums)
        ret = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(len(ret)):
            ret[i] = right[i] * left[i]
        return ret
        


        