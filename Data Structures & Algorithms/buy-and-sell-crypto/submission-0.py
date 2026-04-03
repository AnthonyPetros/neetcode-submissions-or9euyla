class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, maxProfit = prices[0], 0
        for x in prices:
            maxProfit = max(maxProfit, x-p1)
            p1 = min(p1,x)
        return maxProfit