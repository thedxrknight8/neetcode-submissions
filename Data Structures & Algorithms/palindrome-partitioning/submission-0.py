class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # so for instance
        # you split into two at every point
        # check that the first part is a palindrome 
        # and then recurse on the second part
        # if the second part ends up being nothing, then 
        # you are good

        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1

            return True

        ret = []
        temp = []

        def dfs(s):
            if s == "":
                ret.append(temp[:])
                return
            
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if is_palindrome(prefix):
                    temp.append(prefix)
                    suffix = s[i:]
                    dfs(suffix)
                    temp.pop()
        
        dfs(s)
        return ret
                

        
