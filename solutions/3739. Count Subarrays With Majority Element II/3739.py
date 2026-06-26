from typing import List
from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, v):
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        cur = 0
        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            pref.append(cur)

        vals = sorted(set(pref))
        bit = BIT(len(vals))

        ans = 0

        for x in pref:
            idx = bisect_left(vals, x) + 1
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans