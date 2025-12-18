class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        half = k // 2

        orig = [strategy[i] * prices[i] for i in range(n)]
        base = sum(orig)

        pref_orig = [0] * (n + 1)
        pref_price = [0] * (n + 1)

        for i in range(n):
            pref_orig[i + 1] = pref_orig[i] + orig[i]
            pref_price[i + 1] = pref_price[i] + prices[i]

        ans = base

        for i in range(n - k + 1):
            removed = pref_orig[i + k] - pref_orig[i]
            added = pref_price[i + k] - pref_price[i + half]
            ans = max(ans, base - removed + added)

        return ans
