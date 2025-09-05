class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    flips += 1
                else:
                    flips += bit_a + bit_b
        return flips
