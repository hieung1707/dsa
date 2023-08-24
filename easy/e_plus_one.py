"""
Problem:
https://leetcode.com/problems/plus-one/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        remainder = 1

        while idx >= 0 and remainder:
            new_digit = digits[idx] + remainder
            remainder = new_digit // 10

            if remainder:
                new_digit = new_digit % 10

            digits[idx] = new_digit

            idx -= 1

        if remainder:
            digits.insert(0, remainder)

        return digits


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9, 9, 9, 9, 9, 9]))
