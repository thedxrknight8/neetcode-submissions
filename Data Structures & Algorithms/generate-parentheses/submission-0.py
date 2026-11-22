class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the number of closed at a particular moment cannot be greater than the number of open
        # n - closed will answer your query on that 
        
        # with that in mind, you can either select a closed or an open to add 
        # in the following dfs call, you would check and continue if it's still valid
        # all the way until you have len(temp) == n * 2

        sols = []

        def dfs(curr, num_opens):
            if len(curr) - num_opens > num_opens or num_opens > n:
                return
            
            if len(curr) == n * 2:
                sols.append(curr)
                return
            
            # you can either select an open or a closed

            dfs(curr + "(", num_opens + 1)
            dfs(curr + ")", num_opens)
        
        dfs("", 0)
        return sols