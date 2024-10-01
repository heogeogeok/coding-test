from collections import deque
import sys

sys.setrecursionlimit(10000) 

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
visited_rg_same = [[False] * n for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def same_color(a, b):
    if a in ['R', 'G'] and b in ['R', 'G']:
        return True
    return a == b

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
            dfs(nx, ny)

 
def dfs_rg_same(x, y):
    visited_rg_same[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited_rg_same[nx][ny]:
            if graph[x][y] in ['R', 'G'] and graph[nx][ny] in ['R', 'G'] or graph[nx][ny] == graph[x][y]:
                dfs_rg_same(nx, ny)

normal_areas = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            normal_areas += 1


rg_same_areas = 0
for i in range(n):
    for j in range(n):
        if not visited_rg_same[i][j]:
            dfs_rg_same(i, j)
            rg_same_areas += 1

print(str(normal_areas) + ' ' + str(rg_same_areas))