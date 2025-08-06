class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, treeIndex, lo, hi):
        if lo == hi:
            self.tree[treeIndex] = nums[lo]
            return
        mid = (lo + hi) // 2
        self.build(nums, 2 * treeIndex + 1, lo, mid)
        self.build(nums, 2 * treeIndex + 2, mid + 1, hi)
        self.tree[treeIndex] = max(self.tree[2 * treeIndex + 1], self.tree[2 * treeIndex + 2])

    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, treeIndex, lo, hi, i, val):
        if lo == hi:
            self.tree[treeIndex] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * treeIndex + 1, lo, mid, i, val)
        else:
            self._update(2 * treeIndex + 2, mid + 1, hi, i, val)
        self.tree[treeIndex] = max(self.tree[2 * treeIndex + 1], self.tree[2 * treeIndex + 2])

    def query_first(self, target):
        return self._query_first(0, 0, self.n - 1, target)

    def _query_first(self, treeIndex, lo, hi, target):
        if self.tree[treeIndex] < target:
            return -1
        if lo == hi:
            self.update(lo, -1)
            return lo
        mid = (lo + hi) // 2
        leftChild = self.tree[2 * treeIndex + 1]
        if leftChild >= target:
            return self._query_first(2 * treeIndex + 1, lo, mid, target)
        else:
            return self._query_first(2 * treeIndex + 2, mid + 1, hi, target)


class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        ans = 0
        tree = SegmentTree(baskets)
        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                ans += 1
        return ans
