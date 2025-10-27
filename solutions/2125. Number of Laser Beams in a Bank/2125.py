class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        counts = [row.count('1') for row in bank if '1' in row]
        total_beams = 0
        for i in range(1, len(counts)):
            total_beams += counts[i-1] * counts[i]
        return total_beams
