from collections import deque

# 지도 크기 입력
n = int(input())
# 지도 입력 받기
graph = [list(map(int, input())) for _ in range(n)]

# 방문 여부 배열
visited = [[False] * n for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 집의 개수 (현재 집 1개)

    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 지도를 벗어나지 않고, 연결된 집(1)이면서 방문하지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1  # 집의 개수 증가

    return count

# 단지 개수 및 단지 크기 리스트
complexes = []

# 지도 전체를 순회하면서 단지를 찾음
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:  # 집이 있고 아직 방문하지 않았다면
            complex_size = bfs(i, j)  # DFS로 단지 크기 구하기
            complexes.append(complex_size)  # 단지 크기 추가

# 단지 수 출력
print(len(complexes))
# 단지 크기 오름차순 정렬 후 출력
complexes.sort()
for size in complexes:
    print(size)

# # 상하좌우 이동을 위한 방향 벡터
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# DFS 
# def dfs(x, y):
#     # 현재 위치 방문 처리
#     visited[x][y] = True
#     count = 1  # 집의 개수 (현재 집 1개)

#     # 상하좌우 탐색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # 지도를 벗어나지 않고, 연결된 집(1)이면서 방문하지 않은 곳이라면
#         if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
#             count += dfs(nx, ny)  # 재귀적으로 방문하여 연결된 집의 개수 더하기

#     return count