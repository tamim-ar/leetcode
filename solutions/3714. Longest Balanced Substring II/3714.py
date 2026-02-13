class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # 1) k=1: longest run of same character
        best1 = 1
        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                run = 1
            if run > best1:
                best1 = run

        # prefix counts
        a = b = c = 0

        # 3) k=3: need (a-b, a-c) same at two prefix positions
        first3 = {(0, 0): 0}
        best3 = 0

        # 2) k=2: for each pair, key = (count(third), diff(pair))
        # pairs: (x,y,z) => x and y must be equal in substring, z absent
        pairs = [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')]
        first2 = []
        for _ in pairs:
            first2.append({(0, 0): 0})
        best2 = 0

        for i, ch in enumerate(s, start=1):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            # k=3
            key3 = (a - b, a - c)
            if key3 in first3:
                best3 = max(best3, i - first3[key3])
            else:
                first3[key3] = i

            # k=2 (3 variants)
            counts = {'a': a, 'b': b, 'c': c}
            for idx, (x, y, z) in enumerate(pairs):
                diff = counts[x] - counts[y]
                kz = counts[z]
                key2 = (kz, diff)
                mp = first2[idx]
                if key2 in mp:
                    best2 = max(best2, i - mp[key2])
                else:
                    mp[key2] = i

        return max(best1, best2, best3)
