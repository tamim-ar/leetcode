class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        segs = []
        mp = {}
        for x, y in points:
            mp[y] = mp.get(y, 0) + 1
        s = 0
        for _, cnt in mp.items():
            if cnt >= 2:
                k = (cnt * (cnt - 1) // 2) % MOD
                segs.append(k)
                s = (s + k) % MOD
        total = 0
        for i in range(len(segs)):
            s = (s - segs[i]) % MOD
            total = (total + (segs[i] * s) % MOD) % MOD
        return total
