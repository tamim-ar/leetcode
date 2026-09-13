class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        # Store coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        # Count frequencies of each displacement vector (dr, dc)
        shift_counts = {}
        max_overlap = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Calculate required shift vector to align (r1, c1) with (r2, c2)
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] = shift_counts.get(shift, 0) + 1
                max_overlap = max(max_overlap, shift_counts[shift])

        return max_overlap