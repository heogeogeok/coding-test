N = int(input())
stack = []

for _ in range(N):
    command = input().split()
    a = command[0]

    if a == 'push':
        b = command[1]
        stack.append(b)
    elif a == 'pop':
        print(stack.pop() if stack else -1)
    elif a == 'size':
        print(len(stack))
    elif a == 'empty':
        print(1 if not stack else 0)
    elif a == 'top':
        print(stack[-1] if stack else -1)