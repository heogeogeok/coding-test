T = int(input())

for _ in range(T):
    stack = []
    is_valid = True
    for s in input():
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                is_valid = False
                break
    if is_valid:
        if stack:
            print('YES')
        else:
            print('NO')