class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1

        # Step 1: Count all 0s (safe to include)
        count = s.count('0')

        # Step 2: Process from right to left for 1s
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                if power <= k and value + power <= k:
                    value += power
                    count += 1
                else:
                    break
            power <<= 1  # power = 2^bit_position
            if power > k:
                break

        return count