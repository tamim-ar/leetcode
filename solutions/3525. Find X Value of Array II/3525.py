from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)

        class SegmentTree:
            def __init__(self, nums):
                self.n = len(nums)
                self.tree = [
                    [1 % k, [0] * k]
                    for _ in range(4 * self.n)
                ]
                self.build(1, 0, self.n - 1, nums)

            def merge(self, left, right):
                left_prod, left_cnt = left
                right_prod, right_cnt = right

                prod = (left_prod * right_prod) % k
                cnt = left_cnt[:]

                for r in range(k):
                    cnt[(left_prod * r) % k] += right_cnt[r]

                return [prod, cnt]

            def build(self, node, l, r, nums):
                if l == r:
                    v = nums[l] % k
                    cnt = [0] * k
                    cnt[v] = 1
                    self.tree[node] = [v, cnt]
                    return

                mid = (l + r) // 2

                self.build(node * 2, l, mid, nums)
                self.build(node * 2 + 1, mid + 1, r, nums)

                self.tree[node] = self.merge(
                    self.tree[node * 2],
                    self.tree[node * 2 + 1]
                )

            def update(self, node, l, r, pos, value):
                if l == r:
                    v = value % k
                    cnt = [0] * k
                    cnt[v] = 1
                    self.tree[node] = [v, cnt]
                    return

                mid = (l + r) // 2

                if pos <= mid:
                    self.update(node * 2, l, mid, pos, value)
                else:
                    self.update(node * 2 + 1, mid + 1, r, pos, value)

                self.tree[node] = self.merge(
                    self.tree[node * 2],
                    self.tree[node * 2 + 1]
                )

            def query(self, node, l, r, ql, qr):
                if ql <= l and r <= qr:
                    return self.tree[node]

                mid = (l + r) // 2

                if qr <= mid:
                    return self.query(node * 2, l, mid, ql, qr)

                if ql > mid:
                    return self.query(node * 2 + 1, mid + 1, r, ql, qr)

                left = self.query(node * 2, l, mid, ql, qr)
                right = self.query(node * 2 + 1, mid + 1, r, ql, qr)

                return self.merge(left, right)

        tree = SegmentTree(nums)
        ans = []

        for index, value, start, x in queries:
            tree.update(1, 0, n - 1, index, value)

            result = tree.query(
                1, 0, n - 1,
                start, n - 1
            )

            ans.append(result[1][x])

        return ans