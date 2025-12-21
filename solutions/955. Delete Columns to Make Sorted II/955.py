class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        sorted_ok = [False] * (n - 1)
        ans = 0
        
        for c in range(m):
            bad = False
            for i in range(n - 1):
                if not sorted_ok[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            if bad:
                ans += 1
            else:
                for i in range(n - 1):
                    if strs[i][c] < strs[i + 1][c]:
                        sorted_ok[i] = True
        return ans
