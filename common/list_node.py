# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        output = []
        while current_node:
            output.append(str(current_node.val))
            current_node = current_node.next

        return " - ".join(output)

    @classmethod
    def from_list(cls, node_list):
        if not node_list:
            return None

        first_node = cls(node_list[0])
        current_node = first_node

        for i in range(1, len(node_list)):
            next_node = cls(node_list[i])
            current_node.next = next_node
            current_node = next_node

        return first_node
