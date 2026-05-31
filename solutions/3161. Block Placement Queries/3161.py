from bisect import bisect_left

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, val)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, val)

        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        return max(
            self.query(node * 2, l, mid, ql, qr),
            self.query(node * 2 + 1, mid + 1, r, ql, qr)
        )


class Solution:
    def getResults(self, queries):
        mx = max(q[1] for q in queries)

        obstacles = [0, mx]
        seg = SegmentTree(mx + 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                i = bisect_left(obstacles, x)

                left = obstacles[i - 1]
                right = obstacles[i]

                obstacles.insert(i, x)

                seg.update(1, 0, mx, x, x - left)
                seg.update(1, 0, mx, right, right - x)

            else:
                x, sz = q[1], q[2]

                i = bisect_left(obstacles, x + 1)

                left_obstacle = obstacles[i - 1]

                best = seg.query(1, 0, mx, 0, x)

                best = max(best, x - left_obstacle)

                ans.append(best >= sz)

        return ans