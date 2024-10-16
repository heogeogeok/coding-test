import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1: 
        dp[i] = stairs[i]
    elif i == 2:
        dp[i] = stairs[i] + stairs[i-1]
    else:
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])