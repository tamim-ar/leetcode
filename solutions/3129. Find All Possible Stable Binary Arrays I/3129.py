class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache

        @lru_cache(None)
        def dp(z, o, last, count):
            if z == 0 and o == 0:
                return 1
            
            ans = 0
            
            if z > 0:
                if last != 0:
                    ans = (ans + dp(z-1, o, 0, 1)) % MOD
                elif count < limit:
                    ans = (ans + dp(z-1, o, 0, count+1)) % MOD
            
            if o > 0:
                if last != 1:
                    ans = (ans + dp(z, o-1, 1, 1)) % MOD
                elif count < limit:
                    ans = (ans + dp(z, o-1, 1, count+1)) % MOD
            
            return ans % MOD
        
        return (dp(zero, one, -1, 0)) % MOD