from collections import Counter
from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
card_counter = Counter(queue)
result = []

while queue:
    queue.rotate(-K + 1)
    result.append(queue.popleft())

print(f'<{", ".join(map(str, result))}>')
