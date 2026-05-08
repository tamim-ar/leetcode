from collections import defaultdict, deque
from math import isqrt
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        max_val = max(nums)

        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False

        for i in range(2, isqrt(max_val) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False

        divisible = defaultdict(list)

        for i, x in enumerate(nums):
            temp = x
            factors = set()

            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    factors.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp > 1:
                factors.add(temp)

            for f in factors:
                divisible[f].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                val = nums[i]

                if is_prime[val] and val not in used_prime:
                    used_prime.add(val)

                    for nxt in divisible[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

            steps += 1

        return -1