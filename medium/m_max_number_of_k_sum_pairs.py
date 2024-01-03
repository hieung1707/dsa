"""
Problem:
https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Approach: External memory
    Time complexity: O(n)
    Memory complexity: O(n)
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        no_ops = 0

        for num in nums:
            if num in d and d[num]:
                d[num].pop(0)
                no_ops += 1
            else:
                diff = k - num
                if diff > 0:
                    if diff not in d:
                        d[diff] = []
                    d[diff].append(num)

        return no_ops

    """
    Approach: 2 pointers
    The solution is the same as m_container_with_most_water, if you sort the array
    Time complexity: O(n logn)
    Memory complexity: O(1)
    """
    def maxOperationTwoPointer(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        no_ops = 0

        while start < end:
            total = nums[start] + nums[end]
            if total == k:
                start += 1
                end -= 1
                no_ops += 1
            elif total > k:
                end -= 1
            else:
                start += 1

        return no_ops


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations(nums=[1, 2, 3, 4], k=5))
    print(solution.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
    print(solution.maxOperations(nums=[4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], k=2))
    print(solution.maxOperations(nums=[2, 2, 2, 3, 1, 1, 4, 1], k=4))
