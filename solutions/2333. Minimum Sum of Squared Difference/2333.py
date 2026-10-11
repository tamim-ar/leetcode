from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)

        for i in range(len(diff)):
            level = diff[i + 1] if i + 1 < len(diff) else 0
            needed = (diff[i] - level) * (i + 1)

            if k >= needed:
                k -= needed
                for j in range(i + 1):
                    diff[j] = level
            else:
                reduction = k // (i + 1)
                remainder = k % (i + 1)

                for j in range(i + 1):
                    diff[j] -= reduction
                    if j < remainder:
                        diff[j] -= 1

                k = 0
                break

            if k == 0:
                break

        return sum(x * x for x in diff)