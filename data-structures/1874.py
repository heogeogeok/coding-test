n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
current = 1
output = []

for num in sequence:
    while current <= num:
        stack.append(current)
        current += 1
        output.append('+')
    
    if stack and stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(output))
