class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dfs(players):
            l, r = 0, len(players) - 1
            while l < r:
                if {players[l], players[r]} == {firstPlayer, secondPlayer}:
                    return [1, 1]
                l += 1
                r -= 1

            next_rounds = set()
            m = len(players)
            pairs = []
            i, j = 0, m - 1
            while i < j:
                pairs.append((players[i], players[j]))
                i += 1
                j -= 1
            if i == j:
                pairs.append((players[i],))

            def backtrack(idx, path):
                if idx == len(pairs):
                    next_rounds.add(tuple(sorted(path)))
                    return
                pair = pairs[idx]
                if len(pair) == 2:
                    a, b = pair
                    if {a, b} == {firstPlayer, secondPlayer}:
                        return
                    if a == firstPlayer or b == firstPlayer:
                        backtrack(idx + 1, path + [firstPlayer])
                    elif a == secondPlayer or b == secondPlayer:
                        backtrack(idx + 1, path + [secondPlayer])
                    else:
                        backtrack(idx + 1, path + [a])
                        backtrack(idx + 1, path + [b])
                else:
                    backtrack(idx + 1, path + [pair[0]])

            backtrack(0, [])
            res = []
            for nxt in next_rounds:
                x, y = dfs(nxt)
                res.append((x, y))
            return [min(x for x, y in res) + 1, max(y for x, y in res) + 1]

        return dfs(tuple(range(1, n + 1)))
