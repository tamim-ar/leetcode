class Solution:
    def numSteps(self, s: str) -> int:
        if s == "1":
            return 0

        steps = 0
        carry = 0
        n = len(s)

        # process from LSB to the 2nd bit (index 1)
        for i in range(n - 1, 0, -1):
            bit = ord(s[i]) - ord('0')
            val = bit + carry

            if val == 0:
                steps += 1          # even -> /2
            elif val == 1:
                steps += 2          # odd -> +1, then /2
                carry = 1
            else:  # val == 2
                steps += 1          # even -> /2 (carry stays 1)
                carry = 1

        # handle MSB
        if carry == 1:
            steps += 1              # "10" -> "1" by one /2

        return steps