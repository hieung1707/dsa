"""
Problem:
https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Time complexity: O(n^2)
    Memory complexity: O(n)
    """
    def equalPairs(self, grid: List[List[int]]) -> int:
        no_pairs = 0
        dim = len(grid)
        start_value_dict = {}

        # find starting values of all columns. we want to get the column indexes of which those values occur.
        for col_index in range(dim):
            col_value = grid[0][col_index]
            if col_value not in start_value_dict:
                start_value_dict[col_value] = []

            start_value_dict[col_value].append(col_index)

        # loop through each row
        for row_index in range(dim):
            # get the first value of each row, check if it matches with any of the starting column values that have
            #   been stored earlier.
            col_value = grid[row_index][0]
            if col_value not in start_value_dict:
                continue

            # if the first row value matches with one or columns containing the same value as start column value,
            # compare the row with corresponding columns for matches
            for col_index in start_value_dict[col_value]:
                col = [grid[r][col_index] for r in range(dim)]
                row = grid[row_index]

                if row == col:
                    no_pairs += 1

        return no_pairs


if __name__ == "__main__":
    solution = Solution()
    print(solution.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
    print(solution.equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
