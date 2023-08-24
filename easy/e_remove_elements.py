"""
Problem:

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Args:
            nums:
            val:

        Returns:

        """
        start = 0
        end = len(nums) - 1
        k = 0

        while start <= end:
            swap = False

            if nums[start] != val:
                start += 1
                k = start
            else:
                swap = True

            if nums[end] == val:
                end -= 1

            if swap and nums[end] != val and start < end:
                k = start + 1
                nums[start], nums[end] = nums[end], nums[start]

        return k

    def removeElement2(self, nums: List[int], val: int) -> int:
        """
        This solution swaps more
        Args:
            nums:
            val:

        Returns:

        """
        swap_idx = 0
        current_idx = 0

        while current_idx < len(nums):
            num = nums[current_idx]

            if num != val:
                if current_idx != swap_idx:
                    nums[current_idx], nums[swap_idx] = nums[swap_idx], nums[current_idx]

                swap_idx += 1

            current_idx += 1

        return swap_idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2))
