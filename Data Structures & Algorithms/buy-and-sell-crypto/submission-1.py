class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        max_profit = 0
        for x in range(len(prices) - 1):
            if prices[l] > prices[r]:
                #l += 1
                l = r # want to shift left to right to get minimum pointer
            else:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            r += 1
        return max_profit
            