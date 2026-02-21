class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for x in range(left, right + 1):
            if x.bit_count() in primes:
                ans += 1
        return ans