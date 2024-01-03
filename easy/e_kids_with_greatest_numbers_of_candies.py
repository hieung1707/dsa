"""
Problem:
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_kid_candies = max(candies)

        return [kid_candies + extraCandies >= max_kid_candies for kid_candies in candies]


if __name__ == "__main__":
    solution = Solution()
