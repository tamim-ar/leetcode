from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1) + Counter(basket2)
        if any(v % 2 != 0 for v in count.values()):
            return -1

        freq = Counter()
        for x in basket1:
            freq[x] += 1
        for x in basket2:
            freq[x] -= 1

        excess = []
        for k, v in freq.items():
            if v > 0:
                excess.extend([k] * (v // 2))
            elif v < 0:
                excess.extend([k] * (-v // 2))

        excess.sort()
        min_val = min(count)

        n = len(excess) // 2
        return sum(min(excess[i], 2 * min_val) for i in range(n))
