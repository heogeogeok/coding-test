n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

def dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

dfs_result = dfs(graph, 1, [])

print(len(dfs_result)-1)