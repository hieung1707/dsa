"""
Problem:
https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])

        if left_sum == right_sum:
            return 0

        for idx in range(1, len(nums)):
            left_sum += nums[idx - 1]
            right_sum -= nums[idx]

            if left_sum == right_sum:
                return idx

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
    print(solution.pivotIndex(nums=[1, 2, 3]))
    print(solution.pivotIndex(nums=[2, 1, -1]))
