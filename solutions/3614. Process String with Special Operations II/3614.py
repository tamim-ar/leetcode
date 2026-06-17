class Solution:
    def processStr(self, s: str, k: int) -> str:
        LIMIT = 10**15

        lengths = [0] * (len(s) + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = min(LIMIT, cur + 1)

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = min(LIMIT, cur * 2)

            else:  # '%'
                lengths[i + 1] = cur

        final_len = lengths[-1]

        if k >= final_len:
            return '.'

        L = final_len

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == L - 1:
                    return ch
                L -= 1

            elif ch == '*':
                if L > 0:
                    L += 1

            elif ch == '#':
                prev = lengths[i]
                k %= prev
                L = prev

            else:  # '%'
                k = L - 1 - k

        return '.'