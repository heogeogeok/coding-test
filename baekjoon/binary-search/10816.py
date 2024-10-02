from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

count = Counter(cards)
for target in targets:
    print(count[target], end=' ')