class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = maxR = 0
        left = 0
        right = len(height) - 1
        ret = 0

        while left < right:
            maxL = max(maxL, height[left])
            maxR = max(maxR, height[right])

            if maxL < maxR:
                ret += max(0, maxL - height[left])
                left += 1
            else:
                ret += max(0, maxR - height[right])
                right -= 1
        
        return ret
            