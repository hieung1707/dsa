"""
Problem:
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
from typing import Optional
from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        prev_val = None
        current_node = head

        while current_node:
            if current_node.val != prev_val:
                prev_node = current_node
                prev_val = current_node.val
            else:
                prev_node.next = current_node.next

            current_node = current_node.next

        return head


if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteDuplicates(ListNode.from_list([])))
