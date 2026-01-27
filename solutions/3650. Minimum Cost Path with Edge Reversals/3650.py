class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from heapq import heappush, heappop

        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]

        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue

            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))

            for v, w in rg[u]:
                nd = d + 2 * w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]