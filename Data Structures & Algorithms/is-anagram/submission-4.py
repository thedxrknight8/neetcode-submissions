class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        s_t = Counter(t)

        return s_c == s_t