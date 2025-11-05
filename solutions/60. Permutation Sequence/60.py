class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = ''
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            res += nums[index]
            nums.pop(index)
            k %= f
        return res
