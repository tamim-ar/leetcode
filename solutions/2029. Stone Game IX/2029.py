class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        a, b, c = cnt

        if b == 0 and c == 0:
            return False

        if a % 2 == 0:
            return b >= 1 and c >= 1

        return abs(b - c) > 2