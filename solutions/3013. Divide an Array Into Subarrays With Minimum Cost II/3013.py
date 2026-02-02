from heapq import heappush, heappop

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 1

        small = []
        large = []
        small_sum = 0

        def add(x):
            nonlocal small_sum
            if len(small) < need:
                heappush(small, -x)
                small_sum += x
            else:
                if small and x < -small[0]:
                    y = -heappop(small)
                    small_sum -= y
                    heappush(large, y)
                    heappush(small, -x)
                    small_sum += x
                else:
                    heappush(large, x)

        def remove(x):
            nonlocal small_sum
            if small and x <= -small[0]:
                small.remove(-x)
                heapq.heapify(small)
                small_sum -= x
                if large:
                    y = heappop(large)
                    heappush(small, -y)
                    small_sum += y
            else:
                large.remove(x)
                heapq.heapify(large)

        for i in range(1, dist + 2):
            add(nums[i])

        ans = nums[0] + small_sum

        for i in range(dist + 2, n):
            add(nums[i])
            remove(nums[i - (dist + 1)])
            ans = min(ans, nums[0] + small_sum)

        return ans
