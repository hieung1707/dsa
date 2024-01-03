"""
Problem:
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Calculate the current area while moving the left and right pointer inward, starting from the edges of the array.
    """

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_area = 0

        while left <= right:
            wall_height = min(height[left], height[right])
            area = (right - left) * wall_height
            if area > current_area:
                current_area = area

            if height[left] <= wall_height:
                left += 1
            else:
                right -= 1

        return current_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea([1, 1]))
    print(solution.maxArea(
        [76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111, 115,
         76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20, 185, 171,
         23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125, 143, 12, 76,
         192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81, 163, 146, 75, 92,
         198, 126, 191]))
