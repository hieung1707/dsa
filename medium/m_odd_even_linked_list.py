"""
Problem:
https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head_node = None
        even_node = None
        current_node = head
        last_node = None

        idx = 0
        while current_node:
            if idx % 2 != 0:
                next_node = current_node.next
                current_node.next = None

                if not even_node:
                    even_node = current_node
                    even_head_node = even_node
                else:
                    even_node.next = current_node
                    even_node = even_node.next

                current_node = next_node
                last_node.next = next_node
            else:
                last_node = current_node
                current_node = current_node.next
            idx += 1

        if last_node:
            last_node.next = even_head_node

        return head


if __name__ == "__main__":
    solution = Solution()
    print(solution.oddEvenList(ListNode.from_list([1, 2, 3, 4, 5])))
    # print(solution.oddEvenList(ListNode.from_list([2, 1, 3, 5, 6, 4, 7])))
