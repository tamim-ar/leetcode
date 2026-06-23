class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # dp_inc[x] = ways where last relation is increasing and last value = x
        # dp_dec[x] = ways where last relation is decreasing and last value = x
        
        dp_inc = [0] * m
        dp_dec = [0] * m
        
        # length = 2
        for j in range(m):
            dp_inc[j] = j          # choose first value < current
            dp_dec[j] = m - 1 - j  # choose first value > current
        
        if n == 2:
            return sum(dp_inc + dp_dec) % MOD
        
        for _ in range(3, n + 1):
            new_inc = [0] * m
            new_dec = [0] * m
            
            # prefix sums
            pre_inc = [0] * (m + 1)
            pre_dec = [0] * (m + 1)
            
            for i in range(m):
                pre_inc[i + 1] = (pre_inc[i] + dp_inc[i]) % MOD
                pre_dec[i + 1] = (pre_dec[i] + dp_dec[i]) % MOD
            
            total_inc = pre_inc[m]
            total_dec = pre_dec[m]
            
            for x in range(m):
                # To end at x with last move increasing:
                # previous value y < x, and previous move must be decreasing
                new_inc[x] = pre_dec[x]
                
                # To end at x with last move decreasing:
                # previous value y > x, and previous move must be increasing
                new_dec[x] = (total_inc - pre_inc[x + 1]) % MOD
            
            dp_inc, dp_dec = new_inc, new_dec
        
        return (sum(dp_inc) + sum(dp_dec)) % MOD