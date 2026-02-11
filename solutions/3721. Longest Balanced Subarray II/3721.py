from typing import List, Optional

class SegTree:
    def __init__(self, n: int):
        self.n = n
        size = 4 * n
        self.mn = [0] * size
        self.mx = [0] * size
        self.lazy = [0] * size

    def _apply(self, idx: int, val: int):
        self.mn[idx] += val
        self.mx[idx] += val
        self.lazy[idx] += val

    def _push(self, idx: int):
        if self.lazy[idx] != 0:
            v = self.lazy[idx]
            self._apply(idx * 2, v)
            self._apply(idx * 2 + 1, v)
            self.lazy[idx] = 0

    def range_add(self, ql: int, qr: int, val: int):
        def dfs(idx: int, l: int, r: int):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                self._apply(idx, val)
                return
            self._push(idx)
            m = (l + r) // 2
            dfs(idx * 2, l, m)
            dfs(idx * 2 + 1, m + 1, r)
            self.mn[idx] = min(self.mn[idx * 2], self.mn[idx * 2 + 1])
            self.mx[idx] = max(self.mx[idx * 2], self.mx[idx * 2 + 1])

        dfs(1, 0, self.n - 1)

    def find_leftmost_zero(self, ql: int, qr: int) -> Optional[int]:
        def dfs(idx: int, l: int, r: int) -> Optional[int]:
            if qr < l or r < ql:
                return None
            if self.mn[idx] > 0 or self.mx[idx] < 0:
                return None
            if l == r:
                return l
            self._push(idx)
            m = (l + r) // 2
            left = dfs(idx * 2, l, m)
            if left is not None:
                return left
            return dfs(idx * 2 + 1, m + 1, r)

        return dfs(1, 0, self.n - 1)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegTree(n)
        last = {}  # value -> last index
        ans = 0

        for i, x in enumerate(nums):
            is_even = (x % 2 == 0)

            # If x existed before, remove its old last-occurrence contribution
            if x in last:
                old = last[x]
                if is_even:
                    # removing an even decreases E(l) by 1 for all l <= old => diff -= 1
                    st.range_add(0, old, -1)
                else:
                    # removing an odd decreases O(l) by 1 for all l <= old => diff += 1
                    st.range_add(0, old, +1)

            # Add new last-occurrence contribution at i
            last[x] = i
            if is_even:
                # adding an even increases E(l) for l <= i => diff += 1
                st.range_add(0, i, +1)
            else:
                # adding an odd increases O(l) for l <= i => diff -= 1
                st.range_add(0, i, -1)

            # Find smallest l in [0..i] with diff[l] == 0
            l0 = st.find_leftmost_zero(0, i)
            if l0 is not None:
                ans = max(ans, i - l0 + 1)

        return ans
