class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def dfs(s):
            if len(res) >= k:
                return
            
            if len(s) == n:
                res.append(s)
                return
            
            for c in "abc":
                if not s or s[-1] != c:
                    dfs(s + c)
        
        dfs("")
        
        return res[k-1] if k <= len(res) else ""