class Solution:
    def findKthSmallest(self, coins, k):
        left = 1
        right = min(coins) * k

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def count(x):
            n = len(coins)
            total = 0

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm // gcd(lcm, coins[i]) * coins[i]

                        if lcm > x:
                            break

                if lcm > x:
                    continue

                if bits % 2:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left