class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        """
        Dynamic programming solution for maximizing profit from stock investments.

        Args:
            present: List of current prices for each stock
            future: List of future prices for each stock
            budget: Total available budget for investments

        Returns:
            Maximum profit achievable within the budget
        """
        n = len(present)

        # Initialize DP table: dp[i][j] represents max profit using first i stocks with budget j
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            current_price = present[i - 1]
            future_price = future[i - 1]

            for current_budget in range(budget + 1):
                # Option 1: Don't buy the current stock
                dp[i][current_budget] = dp[i - 1][current_budget]

                # Option 2: Buy the current stock if profitable and within budget
                if current_budget >= current_price and future_price > current_price:
                    profit_from_current = future_price - current_price
                    dp[i][current_budget] = max(
                        dp[i][current_budget],
                        dp[i - 1][current_budget - current_price] + profit_from_current
                    )

        # Return the maximum profit achievable with full budget
        return dp[n][budget]