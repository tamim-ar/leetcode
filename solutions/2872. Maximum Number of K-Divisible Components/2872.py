class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0
        vis = [0] * n

        def dfs(u):
            nonlocal ans
            vis[u] = 1
            s = values[u]
            for v in g[u]:
                if not vis[v]:
                    x = dfs(v)
                    if x % k == 0:
                        ans += 1
                    else:
                        s += x
            return s

        dfs(0)
        return ans + 1
