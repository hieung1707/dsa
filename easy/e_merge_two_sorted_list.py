"""
Problem:
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_ln = None

        if list1 and (not list2 or list1.val < list2.val):
            current_ln = list1
            list1 = list1.next
        elif list2:
            current_ln = list2
            list2 = list2.next

        first_node = current_ln

        while list1 and list2:
            if list1.val < list2.val:
                selected_node = list1
                list1 = list1.next
            else:
                selected_node = list2
                list2 = list2.next

            current_ln.next = selected_node
            current_ln = current_ln.next

        while list1:
            current_ln.next = list1
            list1 = list1.next
            current_ln = current_ln.next

        while list2:
            current_ln.next = list2
            list2 = list2.next
            current_ln = current_ln.next

        return first_node


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode.from_list([1])
    l2 = ListNode.from_list([])
    print(solution.mergeTwoLists(l1, l2))
