from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = 1

        # Special handling for 1
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while True:
                if cnt.get(cur, 0) >= 2:
                    length += 2
                    if cur > 10 ** 9:
                        break
                    cur *= cur
                elif cnt.get(cur, 0) == 1:
                    length += 1
                    break
                else:
                    length -= 1
                    break

            ans = max(ans, length)

        return ans