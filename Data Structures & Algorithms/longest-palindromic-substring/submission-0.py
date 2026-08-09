class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the first character longest substring is just the first character
        # for every character you move along the thing, what do you check?
        # if you add the current character then check if it is a palindrome
        # if a palindrome, take the max between the dp[i - 1] and the dp[i - 1] + 
        # s[i] -> WRONG

        # basically, build a 2D dp-array such that the indexes are represented through
        # the array
        # so for instance, start i at the end of the array; dp[i + 1][j - 1] = False
        # if length 1, will move onwards
        # basically, iterate j onwards to find the substring bounds (j is the end, i
        # is the start). if the inner substring is valid, and the two outer are the same,
        # you have a larger substring, so mark the current pair of i, j as True and then 
        # check to see if that was the largest there is

        resIdx = 0
        ret = 0

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if ret < (j - i + 1):
                        ret = j - i + 1
                        resIdx = i
        
        return s[resIdx: resIdx + ret]

        