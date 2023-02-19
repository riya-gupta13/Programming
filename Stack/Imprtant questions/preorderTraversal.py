class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root->left->right
# Iterative
def preorderTraversal(self, root: TreeNode) -> list[int]:
    # approach
    # we are first adding the root to stack and running while loop till stack is not empty
    # we are frst chkng rght ma dappending stack because LIFO, so that when we pop we get left frst whch we wnt
    # so we add root and then pop from stack and append to answer
    # then we add frst rght of root elemt to stack
    # then left elemnt of root to stack
    # then we pop and add to answer then again we chk rght and so on
    if not root:
        return
    res = []
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res


def preorderTraversalRecursion(self, root: TreeNode) -> list[int]:
    res = []

    def preOrder(root):
        if not root:
            return
        res.append(root.val)
        preOrder(root.left)
        preOrder(root.right)

    preOrder(root)
    return res
