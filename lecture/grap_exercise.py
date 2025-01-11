def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            stack.extend(reversed(graph[node]))

    return visited

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 자식 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



from collections import deque

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


    
class Solution:
    def numIslands(self, grid):
        count = 0
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        def bfs(row, col, grid):
            queue = deque([(row, col)])
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]

            visited[row][col] = True

            while queue:
                cur_row, cur_col = queue.popleft()
                for i in range(4):
                    next_row = cur_row + dr[i]
                    next_col = cur_col + dc[i]
                    if 0 <= next_row < row_len and 0 <= next_col < col_len:
                        if grid[next_row][next_col] == "1" and not visited[next_row][next_col]:
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
        for i in range(row_len):
                for j in range(col_len):
                    if grid[i][j] == "1" and not visited[i][j]:
                        bfs(i, j, grid)
                        count += 1
        return count