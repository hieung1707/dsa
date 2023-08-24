"""
Problem:
https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        strs_len = len(strs)

        for i in range(len(strs[0])):
            if any(len(strs[j]) <= i for j in range(1, strs_len)):
                return longest_prefix

            ch = strs[0][i]
            if any(strs[j][i] != ch for j in range(1, strs_len)):
                return longest_prefix

            longest_prefix += ch

        return longest_prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix(["a"]))
