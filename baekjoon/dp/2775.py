t = int(input())
for _ in range(t):
    k = int(input()) # k층
    n = int(input()) # n호
    
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    # 0층
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] 
    
    print(dp[k][n]) 