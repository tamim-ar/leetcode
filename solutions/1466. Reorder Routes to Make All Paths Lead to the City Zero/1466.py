class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        
        visited = set()
        res = 0

        def dfs(node):
            nonlocal res
            visited.add(node)
            for nei, cost in graph[node]:
                if nei not in visited:
                    res += cost
                    dfs(nei)

        dfs(0)
        return res
