class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

  ##  Time complexity is O(n)
def lca(root, node1, node2):
    # Base Case
    if root is None:
        return None

    if root.data == node1 or root.data == node2:
        return root

    left_lca = lca(root.left, node1, node2)
    right_lca = lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root
    if left_lca:
        return left_lca
    else:
        return right_lca


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
print(lca(root, 4,5).data)
