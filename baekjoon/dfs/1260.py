from collections import deque

# 입력 처리
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

# DFS
def dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

# BFS
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited
        


dfs_result = dfs(graph, v, [])
bfs_result = bfs(graph, v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))