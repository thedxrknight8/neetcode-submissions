class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # take it through the 5 steps
        # 1. find a dag representation
        # in this case, 1 -> 2 -> 3 -> 7
        # or 4 -> 7, to find the number of elements for a given subsequence, we just take numbers that are less
        # than the current number

        # 2. find a subproblem
        # in this case, say we wanted the longest subproblem ending in 7
        # we can go backwards and find every number that is less than the
        # current number and add 7 to the current sequence
        # i.e. you could take 1->7, 4->7, ... or 1->2->7 or, even better, 
        # 1->2->3->7, you find the first number and add the length of the sequence
        # onto the current element (find 3 for 7 and add 1->2->3)

        # 3. find relationships among subproblems
        # LIS(7) = 1 + max(LIS(1), LIS(2), LIS(3), LIS(3)) = 1 + 3 = 4
        
        # 4. generalize the relationship
        # LIS(X) = 1 + max(LIS(K) where K < X)

        # 5. implement the subproblems in order
        # solve in order of indices and run a for loop for j (inner)
        # the find every element with value less than the current
        # take every dp value and take the max and add one for the current element
        # dp[X] = 1 + max(dp[K] for all K), return the max(dp)

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            longest_subsequence = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_subsequence = max(longest_subsequence, dp[j])
            dp[i] = longest_subsequence + 1
        
        return max(dp)
