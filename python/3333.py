from typing import List

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node: int, parent: int, div: int) -> int:
            if div >= 14:  # Since coins[i] <= 10^4, after 14 divisions it becomes 0
                return 0
                
            coin = coins[node] >> div
            # Option 1: Subtract k
            ans1 = coin - k
            # Option 2: Divide by 2
            ans2 = coin >> 1
            
            for child in graph[node]:
                if child != parent:
                    ans1 += dfs(child, node, div)
                    ans2 += dfs(child, node, div + 1)
                    
            return max(ans1, ans2)
            
        return dfs(0, -1, 0)

def _driver():
    param_1 = [[0,1],[0,2],[1,2]]
    param_2 = [5,2,1]
    param_3 = 6
    sol = Solution()
    ret = sol.maximumPoints(param_1, param_2, param_3)
    print(ret)

_driver()
    param_1 = "aabbcc"
    param_2 = 5
    sol = Solution()
    ret = sol.possibleStringCount(param_1, param_2)
    print(ret)

_driver()
