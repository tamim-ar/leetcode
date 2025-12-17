from typing import List
import collections
from functools import cache

class Solution:
    def maxProfit(self, N: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:

        adj = collections.defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)

        @cache
        def c(node, idx, prev):
            if idx == len(adj[node]):
                return [0] * (budget + 1)

            b1 = c(node, idx + 1, prev)
            b2 = f(adj[node][idx], prev)

            res = [0] * (budget + 1)
            for i in range(budget + 1):
                if b1[i] < 0:
                    continue
                for j in range(budget - i + 1):
                    if b2[j] < 0:
                        continue
                    res[i + j] = max(res[i + j], b1[i] + b2[j])
            return res

        @cache
        def f(node, prev):
            dp = c(node, 0, False)

            cost = present[node - 1] // 2 if prev else present[node - 1]
            gain = future[node - 1] - cost

            take = c(node, 0, True)
            for i in range(budget + 1):
                if i + cost <= budget:
                    dp[i + cost] = max(dp[i + cost], take[i] + gain)

            for i in range(1, budget + 1):
                dp[i] = max(dp[i], dp[i - 1])
            return dp

        res = f(1, False)
        return res[budget]
