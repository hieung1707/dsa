"""
Problem:
https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_dict = {}

        for num in arr:
            if num not in occurrence_dict:
                occurrence_dict[num] = 0

            occurrence_dict[num] += 1

        seen = set()
        for no_occurrences in occurrence_dict.values():
            if no_occurrences in seen:
                return False

            seen.add(no_occurrences)

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
    print(solution.uniqueOccurrences(arr=[1, 2]))
    print(solution.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
