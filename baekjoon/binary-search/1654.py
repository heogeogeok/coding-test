import sys
k, n = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]

left, right = 1, max(cables)

while left <= right:
    mid = (left + right) // 2
    
    count = 0 
    for cable in cables:
        count += cable // mid

    if count >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)
    