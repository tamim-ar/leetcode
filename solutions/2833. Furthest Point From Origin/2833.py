class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        u = moves.count('_')
        return abs(l - r) + u