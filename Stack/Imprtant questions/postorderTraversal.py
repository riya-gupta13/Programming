class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left->right->root
def postorderTraversal(self, root: TreeNode) -> list[int]:
    # just same as preorder just change right nd left
    if not root:
        return []
    # Create an array list to store the solution result...
    res = []
    # Create an empty stack and push the root node...
    stack = [root]
    # Loop till stack is empty...
    while stack:
        # Pop a node from the stack...
        node = stack.pop()
        res.append(node.val)
        # Push the left child of the popped node into the stack...
        if node.left:
            stack.append(node.left)
        # Append the right child of the popped node into the stack...
        if node.right:
            stack.append(node.right)
    return res[::-1]
