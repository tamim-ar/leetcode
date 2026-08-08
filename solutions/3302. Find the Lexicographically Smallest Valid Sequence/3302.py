class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # suf[i] = maximum number of characters of word2
        # that can be matched starting from word1[i]
        # with at most one mismatch.
        suf = [0] * (n + 1)

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            if j < 0:
                suf[i] = m
            else:
                suf[i] = m - 1 - j

        ans = []
        i = 0
        j = 0
        used_mismatch = False

        while i < n and j < m:
            # Option 1: use this character as an exact match
            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1

            # Option 2: use our one allowed mismatch
            elif not used_mismatch:
                # After taking i as the mismatch, we need to
                # match word2[j+1:] from word1[i+1:].
                if suf[i + 1] >= m - j - 1:
                    ans.append(i)
                    used_mismatch = True
                    i += 1
                    j += 1
                else:
                    i += 1

            else:
                i += 1

        if j == m:
            return ans

        return []