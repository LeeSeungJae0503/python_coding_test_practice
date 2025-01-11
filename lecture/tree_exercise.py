from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

def levelOrder(root):
    visited = []
    if root is None:
        return visited
    q = deque([root])
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited


def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result

def inorder(root, result=None):
    if root is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result

def postorder(root, result=None):
    if root is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result