"""
Problem:
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        current_node = head

        while current_node:
            n += 1
            current_node = current_node.next

        middle = n // 2
        prev = None
        idx = 0
        current_node = head
        while idx != middle:
            prev = current_node
            current_node = current_node.next
            idx += 1

        if prev:
            prev.next = current_node.next
        else:
            head = current_node.next

        return head


if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteMiddle(head=ListNode.from_list([1, 3, 4, 7, 1, 2, 6])))
    print(solution.deleteMiddle(head=ListNode.from_list([1, 2, 3, 4])))
    print(solution.deleteMiddle(head=ListNode.from_list([2, 1])))
    print(solution.deleteMiddle(head=ListNode.from_list([1])))
