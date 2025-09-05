class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            val = num1 - k * num2
            if val >= k and bin(val).count("1") <= k:
                return k
        return -1
