"""
Problem:
https://leetcode.com/problems/can-place-flowers/
"""
import math
from typing import List


class Solution:
    """
    Explanation:
    - Formula for calculating number of plantable flowers = ceil((no. vacant plots - padding_left - padding_right) / 2)
    Why -1? Because the problem states that every flower must not be planted near another flower. So this means
    every time  you plant a flower, you have to slip an index.
        + For example, if we have 4 vacant plots [0, 0, 0, 0], we can plant the flowers as [1, 0, 1, 0], or [0, 1, 0, 1]
        => plantable plots = 2. However, if there are flowers adjacent to the left or right of vacant plots
        (1 | [0, 0, 0, 0] | 1), you will have to remove the left-most and right-most plots as it is no longer plantable.
        This reduces vacant space to [x, 0, 0, x] => no. plantable plots = 1, either [x, 0, 1, x] or [x, 1, 0, x]
    - Edge cases the vacant space is at the start and at the end of the flowerbed. This would mean
    there won't be adjacent flowers planted at left-most or right-most position of the vacant space.
        + padding_left = 0 (for left-most vacant plots)
        + padding_right = 0 (for right-most vacant plots)
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_start_idx = 0
        remaining = n
        padding_right = 1
        padding_left = 0

        for idx, is_planted in enumerate(flowerbed):
            if is_planted:
                remaining -= math.ceil((idx - empty_start_idx - padding_left - padding_right) / 2)

                empty_start_idx = idx + 1
                padding_left = 1

            if remaining <= 0:
                return True

        return remaining - math.ceil((len(flowerbed) - empty_start_idx - padding_left) / 2) <= 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([0, 0, 0, 0, 1, 0, 0, 0, 1], 3))
    print(solution.canPlaceFlowers([0, 0, 0, 1], 1))
    print(solution.canPlaceFlowers([0, 0, 0], 1))
