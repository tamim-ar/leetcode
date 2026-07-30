from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""
        m = 0

        for c, f in cnt.items():
            if f & 1:
                mid = c
            half[ord(c) - ord("a")] = f // 2
            m += f // 2

        LIMIT = 10**6 + 1

        def ways(left):
            res = 1
            rem = left
            for x in half:
                if x:
                    res *= comb(rem, x)
                    if res > LIMIT:
                        return LIMIT
                    rem -= x
            return res

        if ways(m) < k:
            return ""

        first = []

        while m:
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                w = ways(m - 1)

                if w >= k:
                    first.append(chr(i + ord("a")))
                    m -= 1
                    break

                k -= w
                half[i] += 1

        first = "".join(first)
        return first + mid + first[::-1]