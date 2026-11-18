class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # what if we before the cutoff but target is after cutoff? 
        # 6 > 2, but target < 2. so that means target is right side

        # what if we before the cutoff and the target before the cutoff?
        # 6 > 3 and 4 > 3. so that means target is left side
        
        # what if we after the cutoff and the target before the cutoff?
        # 0 < 2 but 0 < 3. so that means target is left side

        # what is we after cutoff and the target after the cutoff?
        # 0 < 2 and 1 < 2. so that means target is right side. 

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] < nums[right]:
                if target > nums[middle]:
                    if target <= nums[right]:
                        # search right
                        left = middle + 1
                    else:
                        right = middle - 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle]:
                    if target >= nums[left]:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    left = middle + 1

            
        return -1
