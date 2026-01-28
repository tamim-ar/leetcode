class Solution:
    def minCost(self, grid, k):
        import heapq

        m, n = len(grid), len(grid[0])
        INF = 10**18

        dist = [[[INF]*(k+1) for _ in range(n)] for __ in range(m)]
        dist[0][0][0] = 0

        cells = sorted([(grid[i][j], i, j) for i in range(m) for j in range(n)])
        unused = [cells[:] for _ in range(k+1)]
        ptr = [0]*(k+1)

        pq = [(0, 0, 0, 0)]

        while pq:
            d, i, j, t = heapq.heappop(pq)
            if d != dist[i][j][t]:
                continue

            if i == m-1 and j == n-1:
                return d

            if j+1 < n and d + grid[i][j+1] < dist[i][j+1][t]:
                dist[i][j+1][t] = d + grid[i][j+1]
                heapq.heappush(pq, (dist[i][j+1][t], i, j+1, t))

            if i+1 < m and d + grid[i+1][j] < dist[i+1][j][t]:
                dist[i+1][j][t] = d + grid[i+1][j]
                heapq.heappush(pq, (dist[i+1][j][t], i+1, j, t))

            if t < k:
                while ptr[t] < len(unused[t]) and unused[t][ptr[t]][0] <= grid[i][j]:
                    _, x, y = unused[t][ptr[t]]
                    if d < dist[x][y][t+1]:
                        dist[x][y][t+1] = d
                        heapq.heappush(pq, (d, x, y, t+1))
                    ptr[t] += 1

        return -1