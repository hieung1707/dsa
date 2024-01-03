"""
Problem:
https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = max_altitude = 0

        for net_gain in gain:
            current_altitude += net_gain
            max_altitude = max(current_altitude, max_altitude)

        return max_altitude


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestAltitude(gain=[-5, 1, 5, 0, -7]))
    print(solution.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))
