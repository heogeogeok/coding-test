K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        if stack:
            stack.pop() 

print(sum(stack)) 