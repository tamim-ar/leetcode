class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def ok(x):
            s = str(x)
            for d in set(s):
                if int(d) != s.count(d):
                    return False
            return True

        x = n + 1
        while True:
            if ok(x):
                return x
            x += 1
