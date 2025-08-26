class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag, max_area = 0, 0
        for l, w in dimensions:
            diag = l * l + w * w
            area = l * w
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
        return max_area
