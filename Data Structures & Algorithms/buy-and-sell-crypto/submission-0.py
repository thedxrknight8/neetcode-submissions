class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # have left be buy and right be sell
        # buy at the lowest
        # so if prices[right] <= prices[left]
        
        left = 0
        right = 1
        ret = 0

        while left < right and right < len(prices):
            ret = max(prices[right] - prices[left], ret)
            if prices[right] < prices[left]:
                left = right
            right += 1
        
        return ret