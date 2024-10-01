import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [0] * (n+1)
depth = [-1] * (n+1)
cnt = 1

def dfs(v, d):
    global cnt
    visited[v] = cnt
    depth[v]= d
    for nx in graph[v]:
        if visited[nx] == 0:
            cnt += 1
            dfs(nx, d+1)

dfs(r, 0)

total = 0
for i in range(1, n+1):
    total += depth[i] * visited[i]

print(total)
