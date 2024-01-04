class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, node_list: list):
        if not node_list:
            return None

        root = TreeNode(val=node_list[0])

        current_level = 1
        accumulated_index = 1
        q = [root]

        while accumulated_index < len(node_list):
            n_nodes = 2 ** current_level

            for lr_values_index in range(0, n_nodes, 2):
                node = q.pop(0)

                l_value = node_list[accumulated_index + lr_values_index]
                if l_value and node:
                    node.left = TreeNode(val=l_value)
                    q.append(node.left)
                else:
                    q.append(None)

                r_value = node_list[accumulated_index + lr_values_index + 1]
                if r_value and node:
                    node.right = TreeNode(val=r_value)
                    q.append(node.right)
                else:
                    q.append(None)

            accumulated_index += n_nodes


if __name__ == "__main__":
    null = None
    TreeNode.from_list([3, 9, 20, null, null, 15, 7])
