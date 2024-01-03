"""
Problem:
https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    The algorithm relies on the fact that if there is an increasing triplet in the array,
        there must be two values, a and b, such that a < b.
    The algorithm keeps track of the two smallest values encountered (a and b).
    If it finds an element greater than both a and b, it means there is an increasing triplet.
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = int(2 ** 31 - 1)
        for num in nums:
            if num <= a:
                a = num
            elif a < num <= b:
                b = num
            elif num > b:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet([1, 2, 3, 4, 5]))
    print(solution.increasingTriplet([6, 7, 1, 2]))
    print(solution.increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(solution.increasingTriplet([4, 5, 2147483647, 1, 2]))
