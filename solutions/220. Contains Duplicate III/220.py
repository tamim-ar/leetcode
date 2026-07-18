class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}
        size = valueDiff + 1

        for i, num in enumerate(nums):
            bucket = num // size

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_bucket = old // size
                del buckets[old_bucket]

        return False