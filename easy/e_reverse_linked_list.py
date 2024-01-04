"""
Problem:
https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = last_node

            last_node = current_node
            current_node = next_node

        return last_node


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseList(ListNode.from_list([1, 2, 3, 4, 5])))
    print(solution.reverseList(ListNode.from_list([1, 2])))
    print(solution.reverseList(ListNode.from_list([])))
