class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# tree is different from graph as graph can have cycle but tree cannot
# every tree is a graph but every graph is not a tree

root = node(1)
n = 16
q = [root]
i = 2
while i < n:
    cur = q.pop(0)  # 1
    cur.left = node(i)
    cur.right = node(i + 1)
    q.append(cur.left)
    q.append(cur.right)
    i += 2

    print(cur.val)
# TRAVERSALS

# Preorder: root left right
# Inorder : left root right
# Postorder: left right root

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


# preorder(root)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


# inorder(root)

def postorder(root):
    if not root:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.val)

# postorder(root)