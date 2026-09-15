class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # best[i] = maximum number of valid palindromes
        # that can be selected from s[0:i]
        best = [0] * (n + 1)

        # Expand around every center
        for center in range(n):
            
            # Odd-length palindromes
            l = r = center

            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1

                if length >= k:
                    best[r + 1] = max(best[r + 1], best[l] + 1)

                l -= 1
                r += 1

            # Even-length palindromes
            l = center
            r = center + 1

            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1

                if length >= k:
                    best[r + 1] = max(best[r + 1], best[l] + 1)

                l -= 1
                r += 1

            # Carry forward
            if center + 1 < n + 1:
                best[center + 1] = max(
                    best[center + 1],
                    best[center]
                )

        return best[n]