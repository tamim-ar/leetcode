class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(t):
            parent = [i for i in range(n)]
            def find(u):
                if parent[u] != u:
                    parent[u] = find(parent[u])
                return parent[u]
            def union(u, v):
                pu, pv = find(u), find(v)
                if pu == pv:
                    return False
                parent[pu] = pv
                return True
            
            comp = n
            for u, v, time in edges:
                if time > t:
                    if union(u, v):
                        comp -= 1
            return comp >= k

        l, r = 0, max((time for _, _, time in edges), default=0)
        ans = 0

        while l <= r:
            m = (l + r) // 2
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
