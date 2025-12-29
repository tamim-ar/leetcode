class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        mp = {}
        for a, b, c in allowed:
            mp.setdefault(a + b, []).append(c)

        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            def build(i: int, nxt: str) -> bool:
                if i == len(row) - 1:
                    return dfs(nxt)
                key = row[i:i+2]
                if key not in mp:
                    return False
                for ch in mp[key]:
                    if build(i + 1, nxt + ch):
                        return True
                return False

            return build(0, "")

        return dfs(bottom)
