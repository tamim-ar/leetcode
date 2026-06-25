from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Build prefix sums of transformed array
        pref = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)

        # Coordinate compression
        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = BIT(len(vals))
        ans = 0

        for x in pref:
            r = rank[x]
            ans += bit.query(r - 1)   # count previous prefix sums < current
            bit.update(r, 1)

        return ans