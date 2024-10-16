def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance # 최소 거리 1, 최대 거리 distance로 설정
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2  # 최소 거리 설정
        current = 0  # 출발 지점
        count = 0  # 제거한 바위 수
        
        # 바위 사이의 거리를 확인하며 제거할지 결정
        for rock in rocks:
            if rock - current < mid:  # 바위 간의 거리가 mid보다 작으면 바위 제거
                count += 1
            else:
                # 거리가 충분하니 바위를 유지하고 현재 위치를 갱신
                current = rock
        
        # 제거한 바위 수가 n 이하이면 가능한 거리
        if count <= n:
            left = mid + 1  # 더 큰 거리를 시도
        else:
            right = mid - 1  # 거리가 너무 크면 범위를 줄임
    
    return right