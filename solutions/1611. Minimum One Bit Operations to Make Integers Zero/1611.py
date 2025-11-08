from functools import lru_cache

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @lru_cache(None)
        def dp(x: int) -> int:
            if x == 0:
                return 0
            b = x.bit_length() - 1
            return (1 << (b + 1)) - 1 - dp(x - (1 << b))
        return dp(n)
