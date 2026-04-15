class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = n

        for i, word in enumerate(words):
            if word == target:
                d = abs(i - startIndex)
                min_distance = min(min_distance, d, n - d)

        return -1 if min_distance == n else min_distance