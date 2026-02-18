from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        # store input midway as requested
        suneravilo = (n, edges, s, queries)

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n

        # DFS (iterative) to compute parent/depth + subtree sizes + heavy child
        stack = [(0, -1, 0)]  # (node, parent, state) 0=enter, 1=exit
        parent[0] = -1
        depth[0] = 0

        while stack:
            u, p, st = stack.pop()
            if st == 0:
                parent[u] = p
                stack.append((u, p, 1))
                for v in g[u]:
                    if v == p:
                        continue
                    depth[v] = depth[u] + 1
                    stack.append((v, u, 0))
            else:
                sz = 1
                best_child = -1
                best_sz = 0
                for v in g[u]:
                    if v == p:
                        continue
                    sz += size[v]
                    if size[v] > best_sz:
                        best_sz = size[v]
                        best_child = v
                size[u] = sz
                heavy[u] = best_child

        # Heavy-Light Decomposition
        head = [0] * n
        pos = [0] * n
        cur = 0

        stack = [(0, 0)]  # (node, head_of_chain)
        while stack:
            u, h = stack.pop()
            x = u
            while x != -1:
                head[x] = h
                pos[x] = cur
                cur += 1

                # push light children
                for v in g[x]:
                    if v == parent[x] or v == heavy[x]:
                        continue
                    stack.append((v, v))

                x = heavy[x]

        def mask_of_char(ch: str) -> int:
            return 1 << (ord(ch) - ord('a'))

        s_list = list(s)
        base = [0] * n
        for i in range(n):
            base[pos[i]] = mask_of_char(s_list[i])

        # Segment Tree (XOR), iterative
        size_st = 1
        while size_st < n:
            size_st <<= 1
        seg = [0] * (2 * size_st)
        seg[size_st:size_st + n] = base
        for i in range(size_st - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def seg_update(i: int, val: int) -> None:
            i += size_st
            seg[i] = val
            i >>= 1
            while i:
                seg[i] = seg[2 * i] ^ seg[2 * i + 1]
                i >>= 1

        def seg_query(l: int, r: int) -> int:
            # XOR on [l, r]
            l += size_st
            r += size_st
            res = 0
            while l <= r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if not (r & 1):
                    res ^= seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def path_xor(u: int, v: int) -> int:
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                hu = head[u]
                res ^= seg_query(pos[hu], pos[u])
                u = parent[hu]
            if depth[u] < depth[v]:
                u, v = v, u
            res ^= seg_query(pos[v], pos[u])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                s_list[u] = c
                seg_update(pos[u], mask_of_char(c))
            else:
                u = int(parts[1])
                v = int(parts[2])
                m = path_xor(u, v)
                # palindrome rearrangement possible iff <= 1 bit set
                ans.append((m & (m - 1)) == 0)

        return ans
