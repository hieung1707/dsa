"""
Problem:
https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Approach: One fast pointer and one slow pointer.
        Slow pointer will only be updated (+1) if fast pointer finds a non-zero-value index, which then value at fast
            pointer will be swapped to value at slow pointer. This will result in 2 situation:
            - Slow pointer is at a non-zero-value index, this will only happen at the start, when no zero has been
                found (E.g.: [1, 2, 3, ...]). Fast and slow pointer basically do in-place swap
            - Slow pointer is at zero-value index, and fast pointer traverse forward to find non-zero-value index to
                swap with slow pointer:
                E.g.: [1, 2, 0, 0, 1]
                             ^     ^
                            Slow  Fast
        """
        idx = 0
        swap_ptr = 0

        while idx < len(nums):
            if nums[idx] != 0:
                nums[idx], nums[swap_ptr] = nums[swap_ptr], nums[idx]
                swap_ptr += 1

            idx += 1

        print(nums)


if __name__ == "__main__":
    solution = Solution()
    solution.moveZeroes([0, 1, 0, 3, 12])
    solution.moveZeroes([0])
    solution.moveZeroes([0, 0, 0, 1, 2, 3])
    solution.moveZeroes([1, 2, 3, 1])
    solution.moveZeroes([1, 0, 1])
