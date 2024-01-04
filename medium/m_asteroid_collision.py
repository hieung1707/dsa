"""
Problem:
https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def get_direction(self, asteroid: int):
        if asteroid > 0:
            return 1

        return 0

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision_stack = []

        for asteroid in asteroids:
            direction = self.get_direction(asteroid)
            exploded = False
            # One thing to take note is the direction of each asteroid
            # If an asteroid goes left (size < 0) and the other go right (size > 0). They will never collide despite
            # having different directions
            # Example: [-2, -1, 1, 2]
            # Direction: <   <  >  >

            while collision_stack and self.get_direction(collision_stack[-1]) - direction > 0:
                facing_asteroid = collision_stack.pop()
                asteroid_size = abs(asteroid)
                facing_asteroid_size = abs(facing_asteroid)

                if asteroid_size > facing_asteroid_size:
                    # facing asteroid exploded, current asteroid on its way to destroy or to be destroyed
                    # by the other asteroids
                    continue
                elif asteroid_size < facing_asteroid_size:
                    # facing asteroid prevails
                    collision_stack.append(facing_asteroid)

                # current asteroid exploded
                exploded = True
                break

            if not exploded:
                collision_stack.append(asteroid)

        return collision_stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.asteroidCollision(asteroids=[5, 10, -5]))
    print(solution.asteroidCollision(asteroids=[8, -8]))
    print(solution.asteroidCollision(asteroids=[10, 2, -5]))
    print(solution.asteroidCollision(asteroids=[-2, -1, 1, 2]))
