import sys
sys.setrecursionlimit(10000) 

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, graph, visited, n, m):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny, graph, visited, n, m)
    

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    worm_count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, graph, visited, n, m)
                worm_count += 1
    
    print(worm_count)
