class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from heapq import heappush, heappop

        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]

        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            d, u, used = heappop(pq)
            if d > dist[u][used]:
                continue

            for v, w in g[u]:
                if d + w < dist[v][used]:
                    dist[v][used] = d + w
                    heappush(pq, (d + w, v, used))

            if used == 0:
                for v, w in rg[u]:
                    nd = d + 2 * w
                    if nd < dist[v][1]:
                        dist[v][1] = nd
                        heappush(pq, (nd, v, 1))

        ans = min(dist[n - 1])
        return -1 if ans == INF else ans