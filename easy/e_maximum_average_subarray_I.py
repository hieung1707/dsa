"""
Problem:
https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Approach: Sliding windows
    Time Complexity: O(n)
    Memory complexity: O(1)
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = max_sum = sum(nums[:k])

        for idx in range(len(nums) - k):
            current_sum = current_sum - nums[idx] + nums[idx + k]
            max_sum = max(max_sum, current_sum)

        return max_sum / min(len(nums), k)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
    print(solution.findMaxAverage(nums=[5], k=1))
    print(solution.findMaxAverage(nums=[0, 1, 1, 3, 3], k=4))
