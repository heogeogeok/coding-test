import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)

def dfs(v):
    for nx in graph[v]:
        if visited[nx] == 0:
            visited[nx] = v
            dfs(nx)

dfs(1)

for i in range(2, n+1):
    print(visited[i])
