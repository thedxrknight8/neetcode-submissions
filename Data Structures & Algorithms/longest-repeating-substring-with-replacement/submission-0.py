class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we can use left and right pointers
        # essentially, move left until `len(s) - k > most_frequent`

        ret = 0
        left = 0 
        right = 0

        mo = 0        
        m = defaultdict(int)

        while left <= right and right < len(s):
            m[s[right]] += 1
            mo = max(mo, m[s[right]])
            if right - left + 1 - mo > k:
                m[s[left]] -= 1
                left += 1
            ret = max(right - left + 1, ret)
            right += 1

        return ret

