class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]

        def getsum(x1, y1, x2, y2):
            return ps[x2][y2] - ps[x1][y2] - ps[x2][y1] + ps[x1][y1]

        lo, hi, ans = 0, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            ok = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if getsum(i, j, i + mid, j + mid) <= threshold:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
