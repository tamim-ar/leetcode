class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, m):
            if i >= n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            # If we can take all remaining piles
            if i + 2 * m >= n:
                return suffix[i]

            best = 0

            # Take x piles, where 1 <= x <= 2m
            for x in range(1, 2 * m + 1):
                # Current player gets the remaining total
                # minus what the opponent can get.
                opponent = dfs(i + x, max(m, x))
                best = max(best, suffix[i] - opponent)

            memo[(i, m)] = best
            return best

        return dfs(0, 1)