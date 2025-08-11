class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        bit = 1
        while n:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1
        pre = [1]
        for p in powers:
            pre.append((pre[-1] * p) % MOD)
        return [(pre[r+1] * pow(pre[l], MOD-2, MOD)) % MOD for l, r in queries]
