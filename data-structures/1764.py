N, M = map(int, input().split())

a = set()
b = set()

for _ in range(N):
    a.add(input())

for _ in range(M):
    b.add(input())

both = sorted(a & b)

print(len(both))
print("\n".join(both))
