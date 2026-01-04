class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        for n in nums:
            s = set()
            i = 1
            while i * i <= n:
                if n % i == 0:
                    s.add(i)
                    s.add(n // i)
                    if len(s) > 4:
                        break
                i += 1
            if len(s) == 4:
                ans += sum(s)
        return ans
