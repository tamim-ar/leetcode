class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x):
            s = str(x)
            if len(s) < 3:
                return 0

            w = 0
            for i in range(1, len(s) - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    w += 1
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    w += 1
            return w

        return sum(waviness(x) for x in range(num1, num2 + 1))