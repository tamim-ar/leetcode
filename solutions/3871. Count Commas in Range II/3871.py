class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)

            ans += (end - start + 1) * commas

            start *= 1000
            commas += 1

        return ans