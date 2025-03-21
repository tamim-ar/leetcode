class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return len(citations)
