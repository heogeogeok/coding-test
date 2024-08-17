N = int(input())
queue = []

for _ in range(N):
    command = input().split()
    a = command[0]
    if a == 'push':
        queue.append(int(command[1]))
    elif a == 'pop':
        print(queue.pop(0) if queue else -1)
    elif a == 'size':
        print(len(queue))
    elif a == 'empty':
        print(1 if not queue else 0)
    elif a == 'front':
        print(queue[0] if queue else -1)
    elif a == 'back':
        print(queue[-1] if queue else -1)
