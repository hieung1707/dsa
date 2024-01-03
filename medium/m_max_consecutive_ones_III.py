"""
Problem:
https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    """
    Approach:
    - Store the start index of chain (index = 0 at start)
    - Adding element one by one to the chain, if the difference between current chain value and the length of chain
        (current index - start chain index) is greater than acceptable extension (k), compare and store the maximum
        chain value and move start index of chain by 1 unit.
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        start_idx = 0
        chain = max_cons = 0

        for idx, num in enumerate(nums):
            chain += num
            extended_chain = idx - start_idx

            if extended_chain - chain >= k:
                max_cons = max(max_cons, extended_chain)
                chain -= nums[start_idx]
                start_idx += 1

        max_cons = max(max_cons, min(chain + k, len(nums)))

        return max_cons


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
    print(solution.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
    print(solution.longestOnes(nums=[0, 0, 0, 1], k=4))
