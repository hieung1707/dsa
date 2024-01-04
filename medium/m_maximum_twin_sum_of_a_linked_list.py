"""
Problem:
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current_node = head
        pair = {}
        max_val = 0

        counter = 0
        while current_node:
            pair[counter] = current_node.val

            current_node = current_node.next
            counter += 1

        for idx in range(counter // 2):
            pair_idx = counter - 1 - idx
            max_val = max(max_val, pair[idx] + pair[pair_idx])

        return max_val


if __name__ == "__main__":
    solution = Solution()
    print(solution.pairSum(ListNode.from_list([5, 4, 2, 1])))
    print(solution.pairSum(ListNode.from_list([4, 2, 2, 3])))
    print(solution.pairSum(ListNode.from_list([1, 100000])))
