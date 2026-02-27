class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0

        # Special case: flipping all indices each time
        if k == n:
            # After 1 op: all bits toggle. So only possible if s is all-zeros -> 1, or already all-ones -> 0.
            return 1 if z == n else -1

        # If k is even (< n), reachable parity vectors have even Hamming weight
        if k % 2 == 0 and z % 2 == 1:
            return -1

        # Lower bound: need at least ceil(z/k) ops to get at least z total flips
        m = (z + k - 1) // k

        # We won't need to search far; 2*n is a safe cap for n<=1e5
        # (If it doesn't work by then, it's effectively impossible under constraints above.)
        limit = 2 * n + 5

        while m <= limit:
            total = m * k

            # parity must match
            if (total & 1) == (z & 1):
                # compute maxSum depending on m parity
                if m % 2 == 0:
                    maxSum = n * m - z
                else:
                    maxSum = n * (m - 1) + z

                if z <= total <= maxSum:
                    return m

            m += 1

        return -1