from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1, length):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                ways = 0
                total = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        w, t = dp(pos + 1, ntight, False, 10, 10, 0)
                        ways += w
                        total += t
                    else:
                        if not started:
                            w, t = dp(pos + 1, ntight, True, 10, d, 1)
                            ways += w
                            total += t
                        else:
                            add = 0
                            if length >= 2:
                                if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                    add = 1

                            if length == 1:
                                nprev2, nprev1 = prev1, d
                            else:
                                nprev2, nprev1 = prev1, d

                            w, t = dp(
                                pos + 1,
                                ntight,
                                True,
                                nprev2,
                                nprev1,
                                length + 1
                            )

                            ways += w
                            total += t + add * w

                return (ways, total)

            return dp(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)