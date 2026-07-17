from bisect import bisect_left

class Solution(object):
    def gcdValues(self, nums, queries):
        maxv = max(nums)

        freq = [0] * (maxv + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (maxv + 1)

        for g in range(maxv, 0, -1):
            cnt = 0
            for m in range(g, maxv + 1, g):
                cnt += freq[m]

            pairs = cnt * (cnt - 1) // 2

            m = g * 2
            while m <= maxv:
                pairs -= exact[m]
                m += g

            exact[g] = pairs

        prefix = []
        vals = []
        s = 0
        for g in range(1, maxv + 1):
            if exact[g]:
                s += exact[g]
                prefix.append(s)
                vals.append(g)

        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(vals[idx])

        return ans