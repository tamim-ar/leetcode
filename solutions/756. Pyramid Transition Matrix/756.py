class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        mp = {}
        for a, b, c in allowed:
            mp.setdefault(a + b, []).append(c)

        memo = {}

        def dfs(row: str) -> bool:
            if row in memo:
                return memo[row]
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

            memo[row] = build(0, "")
            return memo[row]

        return dfs(bottom)
