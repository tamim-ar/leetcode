from collections import defaultdict
from bisect import bisect_left, insort

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = [i for i in range(c + 1)]
        
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if pu < pv:
                parent[pv] = pu
            else:
                parent[pu] = pv

        for u, v in connections:
            union(u, v)
        
        group = defaultdict(list)
        for i in range(1, c + 1):
            group[find(i)].append(i)
        
        active = {}
        for g in group:
            active[g] = sorted(group[g])
        
        online = [True] * (c + 1)
        res = []
        
        for t, x in queries:
            if t == 2:
                if online[x]:
                    online[x] = False
                    root = find(x)
                    arr = active[root]
                    i = bisect_left(arr, x)
                    if i < len(arr) and arr[i] == x:
                        arr.pop(i)
            else:
                if online[x]:
                    res.append(x)
                else:
                    root = find(x)
                    arr = active[root]
                    res.append(arr[0] if arr else -1)
        
        return res
