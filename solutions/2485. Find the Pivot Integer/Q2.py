class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        x = int(s ** 0.5)
        return x if x * x == s else -1
