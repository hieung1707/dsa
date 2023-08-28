"""
Problem:
https://leetcode.com/problems/01-matrix/
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ...


if __name__ == "__main__":
    solution = Solution()
    print(solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
