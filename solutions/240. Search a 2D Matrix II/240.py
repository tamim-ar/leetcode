class Solution:
    def searchMatrix(self, matrix, target):
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True

            elif current > target:
                col -= 1

            else:
                row += 1

        return False