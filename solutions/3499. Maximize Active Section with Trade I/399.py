class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = s.count('1')

        t = "1" + s + "1"

        chars = []
        lens = []

        for c in t:
            if chars and chars[-1] == c:
                lens[-1] += 1
            else:
                chars.append(c)
                lens.append(1)

        best = 0

        for i in range(1, len(chars) - 1):
            if chars[i] == '1':
                best = max(best, lens[i - 1] + lens[i + 1])

        return base + best