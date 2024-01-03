"""
Problem:
https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Approach
    """
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen = set(nums2)
        answers = [set() for _ in range(2)]

        for num in nums1:
            if num not in seen:
                answers[0].add(num)

        seen = set(nums1)
        for num in nums2:
            if num not in seen:
                answers[1].add(num)

        return answers

    """
    The easy way: builtin support
    """
    def findDifferenceEasyWay(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [set1 - set2, set2 - set1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
    print(solution.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
