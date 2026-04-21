class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        for a, b in allowedSwaps:
            union(a, b)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        ans = 0
        
        for idxs in groups.values():
            freq = {}
            for i in idxs:
                freq[source[i]] = freq.get(source[i], 0) + 1
            
            for i in idxs:
                if freq.get(target[i], 0) > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1
        
        return ans