class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [0] * (n + 1)
        ones = [0] * (n + 1)

        for i, c in enumerate(s):
            zeros[i+1] = zeros[i] + (c == '0')
            ones[i+1] = ones[i] + (c == '1')

        ans = 0
        max_z = int((n)**0.5) + 5

        for i in range(n):
            for z in range(max_z + 1):
                l = i
                r = n - 1
                target = ones[i] + z*z
                lo, hi = i, n
                while lo < hi:
                    mid = (lo + hi) // 2
                    if ones[mid+1] - ones[i] >= z*z:
                        hi = mid
                    else:
                        lo = mid + 1
                j = lo
                if j == n: 
                    continue
                if zeros[j+1] - zeros[i] == z:
                    ans += 1
        return ans
