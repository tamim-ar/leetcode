class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque
        seen = set()
        q = deque([s])
        ans = s
        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            ans = min(ans, cur)
            t = list(cur)
            for i in range(1, len(t), 2):
                t[i] = str((int(t[i]) + a) % 10)
            added = ''.join(t)
            rotated = cur[-b:] + cur[:-b]
            q.append(added)
            q.append(rotated)
        return ans
