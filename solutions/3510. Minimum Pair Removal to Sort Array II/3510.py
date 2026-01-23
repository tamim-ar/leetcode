from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        prev = list(range(-1, n))
        next = list(range(1, n + 1))
        next[n - 1] = -1

        alive = [True] * n
        heap = []

        for i in range(n - 1):
            heap.append((nums[i] + nums[i + 1], i))
        heapq.heapify(heap)

        bad_cnt = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad_cnt += 1

        ops = 0

        while bad_cnt > 0:
            s, i = heapq.heappop(heap)
            j = next[i]
            if j == -1 or not alive[i] or not alive[j] or nums[i] + nums[j] != s:
                continue

            l = prev[i]
            r = next[j]

            if l != -1 and alive[l] and nums[l] > nums[i]:
                bad_cnt -= 1
            if nums[i] > nums[j]:
                bad_cnt -= 1
            if r != -1 and alive[r] and nums[j] > nums[r]:
                bad_cnt -= 1

            nums[i] += nums[j]
            alive[j] = False
            next[i] = r
            if r != -1:
                prev[r] = i

            if l != -1 and alive[l] and nums[l] > nums[i]:
                bad_cnt += 1
            if r != -1 and alive[r] and nums[i] > nums[r]:
                bad_cnt += 1

            if l != -1:
                heapq.heappush(heap, (nums[l] + nums[i], l))
            if r != -1:
                heapq.heappush(heap, (nums[i] + nums[r], i))

            ops += 1

        return ops
