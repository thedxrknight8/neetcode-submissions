class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        ret = float('inf')

        while left <= right:
            k = (left + right) // 2
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / k)
            
            if hours_taken <= h:
                ret = min(ret, k)
                right = k - 1
            else:
                left = k + 1
        
        return ret