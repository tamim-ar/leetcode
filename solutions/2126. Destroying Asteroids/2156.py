class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        cur = mass

        for asteroid in asteroids:
            if cur < asteroid:
                return False
            cur += asteroid

        return True