class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # you want to prevent searching the entire window in that case
        # for the maximum in the window
        
        # basically, iterate until you get a size of k = 3
        # then keep track of the maximum as you insert elements
        # then when you shift, pop off the last element and check the right
        #  use queue to track all the elements
        # when an element leaves the window, you pop off the queue 
        # whenever you introduce an element, insert in sorted fashion

        # so like [1, 2, 1] -> Q[2, 1]
        # then [2, 1, 0] -> Q[2, 1, 0]
        # then [1, 0, 4] -> Q[4]
        # then [0, 4, 2] -> Q[4, 2]
        # then [4, 2, 6] -> Q[6]

        q = deque()

        ret = []

        for right in range(len(nums)):
            # you need to eliminate older results that are large but out of the window
            # and remove the ones the are smaller than the current
            
            while q and q[0] <= right - k:
                q.popleft()
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if q and right >= k - 1:
                ret.append(nums[q[0]])
        return ret


