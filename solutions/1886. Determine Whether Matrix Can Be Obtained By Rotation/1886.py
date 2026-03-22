class Solution:
    def findRotation(self, mat, target):
        def rotate(matrix):
            # 90 degree clockwise rotation
            return [list(row) for row in zip(*matrix[::-1])]
        
        for _ in range(4):  # try all 4 rotations
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False