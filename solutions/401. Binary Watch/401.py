from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):          # 0..11
            for m in range(60):      # 0..59
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    ans.append(f"{h}:{m:02d}")   # minute always 2 digits
        return ans
