class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        for i in range(n):
            # if even taking the whole suffix can't beat ans, stop
            if n - i <= ans:
                break

            freq = [0] * 26
            distinct = 0
            maxf = 0

            for j in range(i, n):
                idx = ord(s[j]) - 97
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                if freq[idx] > maxf:
                    maxf = freq[idx]

                length = j - i + 1

                # necessary conditions
                if length % distinct != 0:
                    continue
                target = length // distinct
                if maxf != target:
                    continue

                # verify all nonzero counts == target
                ok = True
                for c in freq:
                    if c != 0 and c != target:
                        ok = False
                        break

                if ok:
                    ans = max(ans, length)

        return ans
