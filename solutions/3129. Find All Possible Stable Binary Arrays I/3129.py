class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                if i > 0:
                    for k in range(1, min(limit, i)+1):
                        if i-k >= 0:
                            dp0[i][j] = (dp0[i][j] + dp1[i-k][j]) % MOD
                if j > 0:
                    for k in range(1, min(limit, j)+1):
                        if j-k >= 0:
                            dp1[i][j] = (dp1[i][j] + dp0[i][j-k]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD