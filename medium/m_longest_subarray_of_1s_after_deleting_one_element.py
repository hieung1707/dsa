"""
Problem:
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        last_zero = 0
        end = 0
        max_len = 0
        allowed_skip = 1

        for idx, num in enumerate(nums):
            if num == 0:
                if idx - end > 1:
                    max_len = max(max_len, end + 1 - start)
                    start = idx + 1
                elif not allowed_skip:
                    max_len = max(max_len, end - start)
                    start = last_zero + 1
                else:
                    allowed_skip -= 1

                last_zero = idx

            else:
                end = idx

        max_len = max(max_len, len(nums) - start - 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray(nums=[1, 1, 0, 1]))
    print(solution.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(solution.longestSubarray(nums=[1, 1, 1]))
    print(solution.longestSubarray(nums=[0, 0, 0]))
    print(solution.longestSubarray(nums=[1, 0, 0, 0, 0]))
