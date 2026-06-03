from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(startA, durA, startB, durB):
            ridesB = sorted(zip(startB, durB))
            m = len(ridesB)

            starts = [s for s, _ in ridesB]

            pref_min_dur = [0] * m
            pref_min_dur[0] = ridesB[0][1]
            for i in range(1, m):
                pref_min_dur[i] = min(pref_min_dur[i - 1], ridesB[i][1])

            suff_min_finish = [0] * m
            suff_min_finish[-1] = ridesB[-1][0] + ridesB[-1][1]
            for i in range(m - 2, -1, -1):
                suff_min_finish[i] = min(
                    suff_min_finish[i + 1],
                    ridesB[i][0] + ridesB[i][1]
                )

            ans = float('inf')

            for s, d in zip(startA, durA):
                finish_a = s + d

                pos = bisect_right(starts, finish_a)

                best = float('inf')

                if pos > 0:
                    best = min(best, finish_a + pref_min_dur[pos - 1])

                if pos < m:
                    best = min(best, suff_min_finish[pos])

                ans = min(ans, best)

            return ans

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )