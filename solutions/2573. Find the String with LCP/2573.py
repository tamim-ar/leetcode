class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        res = [''] * n
        cur = 'a'
        
        for i in range(n):
            if res[i] == '':
                if cur > 'z':
                    return ""
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = cur
                cur = chr(ord(cur) + 1)
        
        res = "".join(res)
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return res