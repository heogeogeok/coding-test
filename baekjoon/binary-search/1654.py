import sys
k, n = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]

min_length, max_length = 1, max(cables)

while min_length <= max_length:
    mid = (min_length + max_length) // 2
    count = 0 
    for cable in cables:
        count += cable // mid

    if count >= n:
        min_length = mid + 1
    else:
        max_length = mid - 1

print(max_length)
    