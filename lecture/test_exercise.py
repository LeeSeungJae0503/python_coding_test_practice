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

def preorder(root, result=None):
    if result is None:
        return []
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result

def inorder(root, result=None):
    if root is None:
        return []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result

def postorder(root, result=None):
    if root is None:
        return []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result

#graph--------------------------------------------------------------

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}
start_v = 0

def bfs(graph, start):
    queue = deque([start])
    visited = {start: True}
    result = []

    while queue:
        cur_node = queue.popleft()
        result.append(cur_node)
        for next_node in graph[cur_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = True
    return result

def dfs(graph, cur_node, visited):
    visited[cur_node] = True
    for next_node in graph[cur_node]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
