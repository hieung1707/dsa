"""
Problem:
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def _find(self, nums: List[int], start: int, end: int, target: int):
        if start >= end:
            if nums[start] >= target:
                return start

            return start + 1

        middle = (end + start) // 2

        if nums[middle] >= target:
            return self._find(nums, start, middle, target)
        else:
            return self._find(nums, middle + 1, end, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self._find(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(solution.searchInsert(nums, target))
