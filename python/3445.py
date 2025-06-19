import math
import collections

class Solution:
    def maxDifference(self, s, k):
        def get_status(a, b):
            return ((a & 1) << 1) | (b & 1)

        n = len(s)
        ans = float('-inf')

        for a in '01234':
            for b in '01234':
                if a == b:
                    continue
                
                best = [float('inf')] * 4
                cnt_a = cnt_b = prev_a = prev_b = 0
                left = -1

                for right, ch in enumerate(s):
                    if ch == a: cnt_a += 1
                    if ch == b: cnt_b += 1

                    while right - left >= k and cnt_b - prev_b >= 2:
                        status = get_status(prev_a, prev_b)
                        best[status] = min(best[status], prev_a - prev_b)
                        left += 1
                        if s[left] == a: prev_a += 1
                        if s[left] == b: prev_b += 1

                    status = get_status(cnt_a, cnt_b)
                    if best[status ^ 2] < float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[status ^ 2])

        return ans if ans != float('-inf') else -1
