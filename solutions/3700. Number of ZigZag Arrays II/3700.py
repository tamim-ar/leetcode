class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD
        if n == 2:
            return m * (m - 1) % MOD

        size = 2 * m

        # State vector:
        # [up[0], up[1], ..., up[m-1], down[0], down[1], ..., down[m-1]]
        #
        # up[x]   = number of valid arrays ending at x with last step increasing
        # down[x] = number of valid arrays ending at x with last step decreasing

        T = [[0] * size for _ in range(size)]

        # new_up[x] = sum of down[y] for y < x
        for x in range(m):
            for y in range(x):
                T[x][m + y] = 1

        # new_down[x] = sum of up[y] for y > x
        for x in range(m):
            for y in range(x + 1, m):
                T[m + x][y] = 1

        def mat_mul(A, B):
            rA, cA, cB = len(A), len(A[0]), len(B[0])
            res = [[0] * cB for _ in range(rA)]
            for i in range(rA):
                for k in range(cA):
                    if A[i][k] == 0:
                        continue
                    a = A[i][k]
                    for j in range(cB):
                        res[i][j] = (res[i][j] + a * B[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            while power:
                if power & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return res

        # Base vector for length = 2
        base = [[0] for _ in range(size)]

        # up[x] = number of y < x
        for x in range(m):
            base[x][0] = x

        # down[x] = number of y > x
        for x in range(m):
            base[m + x][0] = m - 1 - x

        # We already have length 2, need to go to length n
        P = mat_pow(T, n - 2)
        vec = mat_mul(P, base)

        ans = 0
        for i in range(size):
            ans = (ans + vec[i][0]) % MOD
        return ans