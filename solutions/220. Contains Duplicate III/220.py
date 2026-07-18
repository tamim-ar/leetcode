class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}
        size = valueDiff + 1

        for i, num in enumerate(nums):
            # Bucket ID (handle negative numbers correctly)
            bucket = num // size
            if num < 0:
                bucket -= 1

            # Same bucket
            if bucket in buckets:
                return True

            # Neighbor buckets
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            # Keep only the last indexDiff elements
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_bucket = old // size
                if old < 0:
                    old_bucket -= 1
                del buckets[old_bucket]

        return False