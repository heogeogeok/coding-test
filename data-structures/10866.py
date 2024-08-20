from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command = input().split()

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        print(dq.popleft() if len(dq) > 0 else -1)
    elif command[0] == 'pop_back':
        print(dq.pop() if len(dq) > 0 else -1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(1 if len(dq) == 0 else 0)
    elif command[0] == 'front':
        print(dq[0] if len(dq) > 0 else -1)
    elif command[0] == 'back':
        print(dq[-1] if len(dq) > 0 else -1)