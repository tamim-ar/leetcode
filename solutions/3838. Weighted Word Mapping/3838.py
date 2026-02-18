from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for w in words:
            total = 0
            for ch in w:
                total += weights[ord(ch) - ord('a')]
            m = total % 26
            res.append(chr(ord('z') - m))  # 0->z, 1->y, ..., 25->a
        return "".join(res)
