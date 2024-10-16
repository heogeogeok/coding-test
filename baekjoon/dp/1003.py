t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 1, 0 # 초기화: a는 0이 호출된 횟수, b는 1이 호출된 횟수
    for _ in range(n):
        a, b = b, a + b 
    print(a, b)

