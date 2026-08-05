from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(u):
            suspicious[u] = True
            for v in graph[u]:
                if not suspicious[v]:
                    dfs(v)

        dfs(k)

        # If any non-suspicious method invokes a suspicious one,
        # nothing can be removed.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Remove all suspicious methods.
        return [i for i in range(n) if not suspicious[i]]