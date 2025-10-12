from typing import List
MOD = 10**9+7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        pow_nums = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m + 1):
                pow_nums[i][c] = pow_nums[i][c - 1] * (nums[i] % MOD) % MOD

        dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for idx in range(n):
            dp2 = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)]
            for used in range(0, m + 1):
                for carry in range(0, m + 1):
                    for ones in range(0, m + 1):
                        val = dp[used][carry][ones]
                        if not val:
                            continue
                        maxc = m - used
                        for c in range(0, maxc + 1):
                            new_used = used + c
                            s = carry + c
                            bit = s & 1
                            new_carry = s >> 1
                            new_ones = ones + bit
                            add = val * pow_nums[idx][c] % MOD * inv_fact[c] % MOD
                            dp2[new_used][new_carry][new_ones] = (dp2[new_used][new_carry][new_ones] + add) % MOD
            dp = dp2

        ans = 0
        for carry in range(0, m + 1):
            pc = bin(carry).count("1")
            for ones in range(0, m + 1):
                if ones + pc == k:
                    ans = (ans + dp[m][carry][ones]) % MOD

        ans = ans * fact[m] % MOD
        return ans
