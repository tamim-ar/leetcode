class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        A = [0] * (n + 1)
        B = [0] * (n + 1)
        A[0], A[1] = 1, 1
        B[0], B[1] = 0, 0
        for i in range(2, n + 1):
            B[i] = (B[i-1] + A[i-2]) % MOD
            A[i] = (A[i-1] + A[i-2] + 2 * B[i-1]) % MOD
        return A[n]
