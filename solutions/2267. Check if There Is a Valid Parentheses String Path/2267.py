class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # Total path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                prev = set()

                if r > 0:
                    prev |= dp[r - 1][c]

                if c > 0:
                    prev |= dp[r][c - 1]

                for balance in prev:
                    if grid[r][c] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    if new_balance >= 0:
                        dp[r][c].add(new_balance)

        return 0 in dp[m - 1][n - 1]