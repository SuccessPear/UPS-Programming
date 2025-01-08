class Solution:
    def __init__(self):
        self.dp = []

    def h(self, prices, k, i, t, can_buy):
        # If we run through the price array of complete k transaction then stop
        if i >= len(prices) or t == k:
            return 0

        
        if self.dp[i][t][can_buy] != -1:
            return self.dp[i][t][can_buy]

        profit = self.h(prices, k, i + 1, t, can_buy)

        if can_buy:
            profit = max(profit, -prices[i] + self.h(prices, k, i + 1, t, 0))
        else:
            profit = max(profit, prices[i] + self.h(prices, k, i + 1, t + 1, 1))

        self.dp[i][t][can_buy] = profit
        return profit

    def maxProfit(self, k, prices):
        n = len(prices)
        self.dp = [[[-1] * 2 for _ in range(k)] for _ in range(n)]
        return self.h(prices, k, 0, 0, 1)
    
sol = Solution()
k = 2
prices =  [3,2,6,5,0,3]
print(sol.maxProfit(k, prices))