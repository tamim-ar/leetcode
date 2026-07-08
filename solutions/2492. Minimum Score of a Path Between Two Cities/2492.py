from typing import List
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        ans = float("inf")

        def dfs(node):
            nonlocal ans
            visited.add(node)

            for nei, w in graph[node]:
                ans = min(ans, w)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return ans