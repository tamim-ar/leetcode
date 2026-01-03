class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba = 6
        abc = 6
        for _ in range(2, n + 1):
            aba, abc = (aba * 3 + abc * 2) % MOD, (aba * 2 + abc * 2) % MOD
        return (aba + abc) % MOD
