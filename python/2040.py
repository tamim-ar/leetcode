from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs_leq(x):
            count = 0

            # Negative in nums1
            for a in neg1:
                # we want b such that a * b <= x → b >= x // a
                # since a is negative and nums2 is sorted, we search from the right
                count += len(nums2) - bisect_left(nums2, (x // a) + (x % a != 0))

            # Zero in nums1
            if x >= 0:
                count += zero1 * len(nums2)

            # Positive in nums1
            for a in pos1:
                # we want b such that a * b <= x → b <= x // a
                count += bisect_right(nums2, x // a)

            return count

        # Split nums1 and nums2 into negative, zero, positive
        neg1 = [a for a in nums1 if a < 0]
        pos1 = [a for a in nums1 if a > 0]
        zero1 = len(nums1) - len(neg1) - len(pos1)
        nums2.sort()

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if count_pairs_leq(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left