class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1     # last position of '1'
        pos = 0
        ans = 0

        while n > 0:
            if n & 1:
                if last != -1:
                    ans = max(ans, pos - last)
                last = pos
            n >>= 1
            pos += 1

        return ans