class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # essentially, you would set up the counter for t
        # then iterate through everything in s and then when you
        # have everything you need, then you start pulling back left

        res = [-1, -1]
        resLen = float('inf')

        left = 0
        right = 0
        t_count = Counter(t)
        s_count = defaultdict(int)

        have, need = 0, len(t_count)

        while left <= right and right < len(s):
            s_count[s[right]] += 1
            if s_count[s[right]] == t_count[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
            right += 1
        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""
            

