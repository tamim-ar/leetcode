class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (rec1[0] < rec2[2] and  # rec1 left < rec2 right
                rec1[2] > rec2[0] and  # rec1 right > rec2 left
                rec1[1] < rec2[3] and  # rec1 bottom < rec2 top
                rec1[3] > rec2[1])     # rec1 top > rec2 bottom