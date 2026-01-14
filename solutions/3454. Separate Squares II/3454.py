class Solution:
    def separateSquares(self, squares):
        xs = set()
        events = []
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        xs = sorted(xs)
        x_id = {x: i for i, x in enumerate(xs)}
        n = len(xs) - 1

        seg_len = [0] * (4 * n)
        cover = [0] * (4 * n)

        def pull(node, l, r):
            if cover[node] > 0:
                seg_len[node] = xs[r + 1] - xs[l]
            elif l == r:
                seg_len[node] = 0
            else:
                seg_len[node] = seg_len[node * 2] + seg_len[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                cover[node] += val
                pull(node, l, r)
                return
            if r < ql or qr < l:
                return
            m = (l + r) // 2
            update(node * 2, l, m, ql, qr, val)
            update(node * 2 + 1, m + 1, r, ql, qr, val)
            pull(node, l, r)

        events.sort()
        total = 0
        prev_y = events[0][0]

        for y, t, x1, x2 in events:
            total += seg_len[1] * (y - prev_y)
            update(1, 0, n - 1, x_id[x1], x_id[x2] - 1, t)
            prev_y = y

        half = total / 2
        seg_len = [0] * (4 * n)
        cover = [0] * (4 * n)
        curr = 0
        prev_y = events[0][0]

        for y, t, x1, x2 in events:
            area = seg_len[1] * (y - prev_y)
            if curr + area >= half:
                return prev_y + (half - curr) / seg_len[1]
            curr += area
            update(1, 0, n - 1, x_id[x1], x_id[x2] - 1, t)
            prev_y = y

        return prev_y
