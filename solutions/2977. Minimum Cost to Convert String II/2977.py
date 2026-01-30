class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        import math
        n = len(source)
        INF = 10**18

        words = {}
        idx = 0
        for a, b in zip(original, changed):
            if a not in words:
                words[a] = idx
                idx += 1
            if b not in words:
                words[b] = idx
                idx += 1

        m = idx
        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for a, b, c in zip(original, changed, cost):
            dist[words[a]][words[b]] = min(dist[words[a]][words[b]], c)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF: continue
                for j in range(m):
                    if dist[k][j] == INF: continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        trie = {}
        end = {}
        for s in words:
            node = trie
            for ch in s:
                node = node.setdefault(ch, {})
            end[id(node)] = s

        dp = [INF]*(n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF: continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            node = trie
            for j in range(i, n):
                if source[j] not in node:
                    break
                node = node[source[j]]
                key = id(node)
                if key in end:
                    s = end[key]
                    L = len(s)
                    if i+L <= n and target[i:i+L] in words:
                        u = words[s]
                        v = words[target[i:i+L]]
                        if dist[u][v] != INF:
                            dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])

        return -1 if dp[n] == INF else dp[n]
