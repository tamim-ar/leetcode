from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lg = (n + 1).bit_length()
        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_max = st_max[j - 1]
            prev_min = st_min[j - 1]
            length = 1 << (j - 1)

            cur_max = [0] * (n - (1 << j) + 1)
            cur_min = [0] * (n - (1 << j) + 1)

            for i in range(len(cur_max)):
                cur_max[i] = max(prev_max[i], prev_max[i + length])
                cur_min[i] = min(prev_min[i], prev_min[i + length])

            st_max.append(cur_max)
            st_min.append(cur_min)
            j += 1

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        def range_value(l, r):
            p = log[r - l + 1]
            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])
            return mx - mn

        def best_split(l, r):
            best_pos = l
            best_val = -1

            for i in range(l, r + 1):
                v = range_value(i, r)
                if v > best_val:
                    best_val = v
                    best_pos = i

            return best_pos, best_val

        heap = []

        for r in range(n):
            pos, val = best_split(0, r)
            heapq.heappush(heap, (-val, 0, pos, r))

        ans = 0

        for _ in range(k):
            val, L, pos, r = heapq.heappop(heap)
            ans += -val

            if L <= pos - 1:
                npos, nval = best_split(L, pos - 1)
                heapq.heappush(heap, (-nval, L, npos, r))

            if pos + 1 <= r:
                npos, nval = best_split(pos + 1, r)
                heapq.heappush(heap, (-nval, pos + 1, npos, r))

        return ans