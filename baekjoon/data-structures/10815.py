N = int(input())
cards = set(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

for query in queries:
    print(1 if query in cards else 0, end=' ')