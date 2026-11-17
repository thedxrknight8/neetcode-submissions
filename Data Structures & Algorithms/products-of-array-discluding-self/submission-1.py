class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        for i in range(1, len(nums)):
            products[i] = nums[i - 1] * products[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            products[i] *= postfix
        
        return products
        
