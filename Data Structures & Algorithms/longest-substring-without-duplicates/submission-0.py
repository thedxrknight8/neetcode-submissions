class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        right = 0
        ret = 0

        while left <= right and right < len(s):
            while s[right] in check and left < right:
                check.remove(s[left])
                left += 1
            
            check.add(s[right])
            ret = max(right - left + 1, ret)
            right += 1
        
        return ret

