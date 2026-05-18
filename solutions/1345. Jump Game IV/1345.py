from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([(0, 0)])
        visited = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            neighbors = graph[arr[i]] + [i - 1, i + 1]

            for nxt in neighbors:
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

            graph[arr[i]].clear()