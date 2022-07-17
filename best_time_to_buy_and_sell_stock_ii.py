class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_ = 0
        for i in range(1, len(prices)):
            min_ = min(min_, prices[i])
            max_ = max(max_, prices[i]-min_);            
        return max_
