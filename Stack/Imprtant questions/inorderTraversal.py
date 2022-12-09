class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left->root->right
# Iterative
def inorderTraversal(self, root: TreeNode) -> list[int]:
    # approach
    # we are traversing till the root is there and  STACK is not empty
    # then we are moving cur in the leftmost and appending in stack
    # when the left node bcmes null menas thre is no next left node then we pop from stack
    # and append in answer then we check its rght
    # like this we can traverse whole tree
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def inorderTraversalRecursion(self, root: TreeNode) -> list[int]:
    # recursion
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res
