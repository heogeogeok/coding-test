def solution(n, times):
    low, high = 1, max(times) * n # 최소 시간 1, 최대 시간은 가장 오래 걸리는 심사관이 모두 처리하는 시간
    while low <= high:
        mid = (low + high) // 2
        # 심사 받은 사람 
        people = 0

        # mid 시간 동안 처리할 수 있는 총 사람 수
        for time in times:
            # 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid // time
        
        # 모든 사람이 처리될 수 있으면 시간을 줄여본다
        if people >= n:
            high = mid - 1
        else:
            low = mid + 1
    return low