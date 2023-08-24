"""
Problem:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_num = None
        current_idx = 0

        for idx, num in enumerate(nums):
            if current_num != num:
                current_num = num
                nums[current_idx] = current_num
                current_idx += 1

        return current_idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
