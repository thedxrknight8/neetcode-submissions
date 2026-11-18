class Solution:
    def findMin(self, nums: List[int]) -> int:
        # say your provided array is [4, 5, 6, 1, 2, 3]

        # in this case, your minimum is 1. your middle would lead 
        # to 6 > nums[-1]. in that case, since the current middle is > 
        # than the end, then the minimum should be somewhere right

        # similarily

        # [6, 1, 2, 3, 4, 5]

        # in this case, your minimum is 1. your middle would lead to
        # 3 < nums[-1]. in that case, since the current middle is less
        # than the end, then the minimum should be on the left 

        # so you check less than nums[right] rather than nums[-1]. if less
        # than, than move to the right. else to the left

        left = 0
        right = len(nums) - 1

        res = -1

        while left <= right:
            middle = (left + right) // 2
            res = nums[middle]
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        
        return res

