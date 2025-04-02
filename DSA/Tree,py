import collections

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Binary Tree Traversal Functions
# Breadth-First Search (BFS) and Depth-First Search (DFS)
def bfs(root):
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

print("BFS:", bfs(root))

def dfs(root):
    if not root:
        return []
    return [root.val] + dfs(root.left) + dfs(root.right)

print("DFS:", dfs(root))


# Depth-First Search (DFS) Traversals
# In-order, Post-order, Pre-order
def in_order(root):
    if not root:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)

def post_order(root):
    if not root:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]

def pre_order(root):
    if not root:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)

print("In_order:", in_order(root))
print("Post_order:", post_order(root))
print("Pre_order:", pre_order(root))


# General Tree Functions
# Level Order Traversal
def level_order(root):
    if not root:
        return []
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

print("Level Order:", level_order(root))

# Height of the Tree

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

print("Height of the tree:", height(root))

# Diameter of the Tree
def diameter(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    return max(left_height + right_height, max(left_diameter, right_diameter))

print("Diameter of the tree:", diameter(root))

# Check if the tree is balanced
def is_balanced(root):
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)

print("Is the tree balanced?", is_balanced(root))

# Check if the tree is symmetric
def is_symmetric(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right)

print("Is the tree (Root) symmetric?", is_symmetric(root))
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(4)
root1.right.left = Node(4)
root1.right.right = Node(3)
print("Is the tree (Root1) symmetric?", is_symmetric(root1))

# Check if the tree is a binary search tree (BST)
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_bst(root.left, min_val, root.val) and
            is_bst(root.right, root.val, max_val))
print("Is the tree (Root) a BST?", is_bst(root))
root2 = Node(4)
root2.left = Node(2)
root2.right = Node(6)
root2.left.left = Node(1)
root2.left.right = Node(3)
root2.right.left = Node(5)
root2.right.right = Node(7)
print("Is the tree (Root2) a BST? ", is_bst(root2))

# Check if the tree is a complete binary tree
def is_complete(root):
    if not root:
        return True
    q = collections.deque()
    q.append(root)
    end = False
    while q:
        node = q.popleft()
        if node:
            if end:
                return False
            q.append(node.left)
            q.append(node.right)
        else:
            end = True
    return True

print("Is the tree (Root) a complete binary tree?", is_complete(root))
root3 = Node(1)
root3.left = Node(2)
root3.right = Node(3)
root3.left.left = Node(4)
# root3.left.right = Node(5)
root3.right.left = Node(6)
root3.right.right = Node(7)

print("Is the tree (Root3) a complete binary tree?", is_complete(root3))

# Check if the tree is a full binary tree
def is_full(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    if root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    return False

print("Is the tree (Root) a full binary tree?", is_full(root))
print("Is the tree (Root1) a full binary tree?", is_full(root1))
print("Is the tree (Root2) a full binary tree?", is_full(root2))
print("Is the tree (Root3) a full binary tree?", is_full(root3))